from PIL import Image

def gray_scale(pixels_2d):
    gray_2d = []

    for row in pixels_2d:
        gray_row = []
        for (r, g, b) in row:
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_row.append(gray)
        gray_2d.append(gray_row)

    return gray_2d


def prepare(image, width, height):
    img = Image.open(image).convert("RGB") # либо работать с одним форматом
    pixels = list(img.getdata())

    width_fact, height_fact = img.size

    # превращаем в 2D массив
    pixels_2d = []
    for y in range(height_fact):
        start = y * width_fact
        end = (y + 1) * width_fact
        row = pixels[start:end]
        pixels_2d.append(row)

    pixels_2d = gray_scale(pixels_2d)
    return pixels_2d
