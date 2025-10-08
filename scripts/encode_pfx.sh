#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 path/to/cert.pfx"
  exit 2
fi

PFX="$1"
if [ ! -f "$PFX" ]; then
  echo "File not found: $PFX"
  exit 3
fi

base64 -w 0 "$PFX"
