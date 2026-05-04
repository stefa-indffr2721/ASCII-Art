def convert(pixels_2d, charset):
    dim = len(charset) - 1

    ascii_2d = []
    for row in pixels_2d:
        ascii_row = []
        for (gray, r, g, b) in row:
            char = charset[int(gray / 255 * dim)]
            ascii_row.append((char, r, g, b))
        ascii_2d.append(ascii_row)

    return ascii_2d