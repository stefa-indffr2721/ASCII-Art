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

    return pixels_2d