from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(path='icon.ico'):
    # Создаём простую иконку 256x256 с буквой Z
    size = (256, 256)
    img = Image.new('RGBA', size, (28, 33, 38, 255))
    draw = ImageDraw.Draw(img)

    # Большая буква Z
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 160)
    except Exception:
        font = ImageFont.load_default()

    w, h = draw.textsize('Z', font=font)
    draw.text(((size[0]-w)/2, (size[1]-h)/2 - 10), 'Z', font=font, fill=(255, 200, 0, 255))

    # Сохраняем несколько размеров в .ico
    sizes = [(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)]
    imgs = [img.resize(s, Image.LANCZOS) for s in sizes]
    imgs[0].save(path, format='ICO', sizes=sizes)
    print(f'Generated icon at {path}')

if __name__ == '__main__':
    os.makedirs(os.getcwd(), exist_ok=True)
    make_icon(os.path.join(os.getcwd(), 'icon.ico'))
from PIL import Image, ImageDraw
import os

# Генерирует простую иконку 256x256 с буквой Z
OUT = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')

size = (256, 256)
img = Image.new('RGBA', size, (30, 30, 30, 255))
d = ImageDraw.Draw(img)

# большой круг
d.ellipse((16, 16, 240, 240), fill=(255, 95, 85, 255))

# буква Z
text = 'Z'
# простой способ: рисуем Z линиями
d.line((70, 60, 186, 60), fill=(255,255,255,255), width=18)
d.line((70, 196, 186, 196), fill=(255,255,255,255), width=18)
d.line((186, 60, 70, 196), fill=(255,255,255,255), width=20)

# Сохраняем в формате .ico (Pillow сделает несколько размеров)
img.save(OUT, sizes=[(256,256), (128,128), (64,64), (48,48), (32,32), (16,16)])
print('Generated icon at', OUT)