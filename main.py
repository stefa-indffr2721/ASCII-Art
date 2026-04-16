#python main.py -i 3.png -w 100 -H 50 -s char.txt -o result.txt
import sys
import argparse

import handling
import converter
import console_writer
from file_writer import FileWriter

CHARSET = " .+*=#@"


def check(parser, parm1, parm2=None):
    if parm1 is None and parm2 is None:
        parser.print_help()
        sys.exit(1)


def get_args():
    parser = argparse.ArgumentParser(prog="ASCII-Art")
    parser.add_argument("-i", "--input", type=str, default=None, help="входное изображение")
    parser.add_argument("-w", "--wight",  type=int, default=None, help="ширина выходного изображения (в символах)")
    parser.add_argument("-H", "--height",  type=int, default=None, help="высота выходного изображения (в символах)")
    parser.add_argument("-s", "--set",  type=str, default=None, help="множество символов (файл)")
    parser.add_argument("-o", "--output", type=str, default=None, help="путь к выходному файлу, если не указано - то на консоль")

    args = parser.parse_args()

    check(parser, args.input)
    check(parser, args.wight, args.height)

    try:
        f = open(args.input)
        f.close()
    except FileNotFoundError:
        print("указанный входной файл не найден")
        sys.exit(1)

    return args


def cout(image, path):
    if path is not None:
        writer = FileWriter(path)
        writer.write(image)
    else:
        writer = console_writer.ConsoleWriter()
        writer.write(image)


def main():
    args = get_args()

    image = handling.prepare(args.input, args.wight, args.height)  # вернёт чб 2d массив пикселей

    # перевод в ASCII-Art
    if not args.set is None:
        with open(args.set) as f:
            charset = f.readline().replace("\n", "")
    else:
        charset = CHARSET

    image_ASCII = converter.convert(image, charset)

    cout(image_ASCII, args.output)


if __name__ == "__main__":
    main()