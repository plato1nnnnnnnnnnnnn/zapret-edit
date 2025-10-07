#!/bin/bash
set -e

# Установка зависимостей
pip install -r requirements.txt

# Сборка exe через PyInstaller
python3 src/generate_pac.py
pyinstaller zapret_proxy_simple.spec

echo "Сборка завершена. Файл находится в папке dist/"
