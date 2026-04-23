import png_opener

def prepare(path_to_image, width, height):
    (pixels, width_fact, height_fact) = png_opener.read_png(path_to_image)

    # превращаем в 2D массив
    pixels_2d = []
    for y in range(height_fact):
        start = y * width_fact
        end = (y + 1) * width_fact
        row = pixels[start:end]
        pixels_2d.append(row)

    pixels_2d = resize(pixels_2d, width_fact, height_fact, width, height)

    return pixels_2d


def resize(pixels_2d, width_fact, height_fact, width, height):
    if width is None and height is None:
        return pixels_2d

    if width is None:
        width = round(height * width_fact / height_fact)
    if height is None:
        height = round(width * height_fact / width_fact)

    result = []
    for y in range(height):
        src_y = int(y / height * height_fact)
        row = []
        for x in range(width):
            src_x = int(x / width * width_fact)
            row.append(pixels_2d[src_y][src_x])
        result.append(row)
    return result