from PIL import Image, ImageDraw, ImageFont
import os


def make_icon(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')

    # Генерируем базовую RGB-иконку 128x128
    size = (128, 128)
    bg_color = (28, 33, 38)
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    # Большая буква Z
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 96)
    except Exception:
        font = ImageFont.load_default()

    try:
        bbox = draw.textbbox((0, 0), 'Z', font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except Exception:
        w, h = font.getsize('Z')

    draw.text(((size[0] - w) / 2, (size[1] - h) / 2 - 6), 'Z', font=font, fill=(255, 200, 0))

    # Список поддерживаемых размеров
    sizes = [(128, 128), (48, 48), (32, 32), (16, 16)]
    # Создаём отдельные изображения для каждого размера
    images = [img.resize(s, Image.LANCZOS).convert('RGB') for s in sizes]
    # Сохраняем ICO — Pillow использует первый image и sizes list
    images[0].save(path, format='ICO', sizes=sizes)
    print(f'Generated icon at {path}')


if __name__ == '__main__':
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    make_icon()