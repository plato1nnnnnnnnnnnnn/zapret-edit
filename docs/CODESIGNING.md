# Code signing guide

This repository supports manual code signing of the Windows installer using a PFX certificate.

Recommended secret names:
- `CODESIGN_PFX` — base64-encoded PFX file content
- `CODESIGN_PFX_PASS` — password for the PFX file

How to prepare your PFX for GitHub Secrets (local machine):

1. Encode the PFX in base64:

```bash
# replace cert.pfx with your certificate file
base64 -w 0 cert.pfx > cert.pfx.base64
```

2. Copy the contents of `cert.pfx.base64` and add it to repository Secrets as `CODESIGN_PFX`. Add the PFX password as `CODESIGN_PFX_PASS`.

3. Run the manual signing workflow `.github/workflows/signing.yml` from the Actions tab, or use the provided script to sign locally.

Security notes:
- Never commit the PFX or its base64 directly into the repository.
- Use repository or organization secrets with limited access.
Code signing (Windows installer)
================================

This document explains how to sign the Windows installer (`ZapretProxySetup.exe`) using a code signing certificate and how to set up a GitHub Actions job to perform signing.

Requirements
- A code signing certificate in PFX format and its password.
- A secure place to store the certificate and password: GitHub Actions secrets.

Recommended secrets (add in repository Settings → Secrets):
- `CODESIGN_PFX` — base64-encoded PFX file (or use a secure storage and download step).
- `CODESIGN_PFX_PASS` — password for the PFX.

High-level steps
1. Add your PFX to the secrets (either as base64 string or upload to a secure artifact store and use a read-only token).
2. Add a signing job to GitHub Actions that runs on `windows-latest` and uses `signtool.exe` (part of Windows SDK) or `osslsigncode` to sign the EXE.
3. Upload the signed artifact as release asset.

Notes
- You will need to ensure the Windows runner has the signing tool available. The `signtool` is available if you install the Windows SDK or use preconfigured runner images. Alternatively, use a self-hosted runner that already has signing tools and the certificate installed.

Security
- Keep your PFX and password secret. Prefer to store PFX in GitHub Secrets as base64 and decode during the workflow into a temporary file.

Example commands (PowerShell inside workflow):
```powershell
# Decode PFX
[System.IO.File]::WriteAllBytes('signing.pfx', [System.Convert]::FromBase64String($env:CODESIGN_PFX))
# Sign with signtool (requires Windows SDK)
& "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\x64\\signtool.exe" sign /f signing.pfx /p $env:CODESIGN_PFX_PASS /tr http://timestamp.digicert.com /td sha256 /fd sha256 "path\\to\\ZapretProxySetup.exe"
```

For more secure/enterprise setups, consider using Azure Key Vault or an external HSM.
