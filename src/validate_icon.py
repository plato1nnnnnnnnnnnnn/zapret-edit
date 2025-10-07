from PIL import Image
import sys

ICON_PATH = 'icon.ico'
REQUIRED_SIZES = {(128, 128), (48, 48), (32, 32), (16, 16)}

try:
    im = Image.open(ICON_PATH)
except Exception as e:
    print(f'ERROR: cannot open {ICON_PATH}: {e}')
    sys.exit(2)

info_sizes = im.info.get('sizes')
if not info_sizes:
    print(f'ERROR: {ICON_PATH} has no sizes metadata')
    sys.exit(3)

if set(info_sizes) >= REQUIRED_SIZES:
    print(f'OK: {ICON_PATH} contains required sizes: {sorted(list(info_sizes))}')
    sys.exit(0)
else:
    print(f'ERROR: {ICON_PATH} missing required sizes. Found: {sorted(list(info_sizes))}, required: {sorted(list(REQUIRED_SIZES))}')
    sys.exit(4)
