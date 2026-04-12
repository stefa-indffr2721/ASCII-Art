def convert(gray_2d, charset):
    dim = len(charset) - 1

    ascii_2d = []
    for row in gray_2d:
        ascii_row = []
        for value in row:
            char = charset[int(value / 255 * dim)]
            ascii_row.append(char)
        ascii_2d.append(ascii_row)

    return ascii_2d