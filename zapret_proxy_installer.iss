; Скрипт для Inno Setup
[Setup]
AppName=Zapret Proxy
AppVersion=1.0
DefaultDirName={pf}\ZapretProxy
DefaultGroupName=Zapret Proxy
OutputDir=dist
OutputBaseFilename=ZapretProxySetup
SetupIconFile=icon.ico
; SetupIconFile was re-enabled after validating generated icon.ico for Inno Setup compatibility

[Files]
; PyInstaller will produce `dist\zapret_proxy.exe` with the updated spec
Source: "dist\\zapret_proxy.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\\config.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\\zapret_proxy.pac"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Запрет Proxy"; Filename: "{app}\zapret_proxy.exe"; IconFilename: "{app}\icon.ico"
Name: "{userstartup}\Запрет Proxy"; Filename: "{app}\zapret_proxy.exe"; IconFilename: "{app}\icon.ico"

[Run]
; После установки — установить AutoConfigURL (только для текущего пользователя)
Filename: "reg.exe"; Parameters: "add HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings /v AutoConfigURL /t REG_SZ /d ""{app}\\zapret_proxy.pac"" /f"; Flags: runhidden

[UninstallRun]
; При удалении — удалить AutoConfigURL
Filename: "reg.exe"; Parameters: "delete HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings /v AutoConfigURL /f"; Flags: runhidden
