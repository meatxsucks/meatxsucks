#!/usr/bin/env python3
"""
Convierte una foto a ASCII art para usar en el perfil de GitHub.

Uso:  python3 photo-to-ascii.py "ruta/foto.jpeg" [ancho] > art.txt
Requiere: pip install Pillow
"""

import sys
from PIL import Image

# Caracteres ordenados por densidad visual (del más oscuro al más claro)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=38):
    (original_width, original_height) = image.size
    # 0.55 porque los caracteres de texto son más altos que anchos
    aspect_ratio = original_height / float(original_width) * 0.55
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))


def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def image_to_ascii(image_path, new_width=38):
    image = Image.open(image_path)
    image = resize_image(grayify(image), new_width)
    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    return "\n".join(
        [ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)]
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 38
    print(image_to_ascii(path, width))
