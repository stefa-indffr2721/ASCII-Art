import sys
import argparse

import handling
import converter
import console_writer

CHARSET = " .+*=#@"

def check(parser, parm1, parm2=None):
    if parm1 == None and parm2 == None:
        parser.print_help()
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="ASCII-Art")
    parser.add_argument("-i", "--input", type=str, default=None, help="входное изображение")
    parser.add_argument("-w", "--wight",  type=int, default=None, help="ширина выходного изображения (в символах)")
    parser.add_argument("-H", "--height",  type=int, default=None, help="высота выходного изображения (в символах)")
    parser.add_argument("-s", "--set",  type=str, default=None, help="множество символов (файл)")
    parser.add_argument("-o", "--output", type=str, default=None, help="путь к выходному файлу")

    args = parser.parse_args()

    # проверка
    check(parser, args.input)
    check(parser, args.wight, args.height)

    # предобработка
    try:
        f = open(args.input)
        f.close()
    except FileNotFoundError:
        # parser.print_help()
        print("файл не найден")
        return


    image = args.input  # путь

    image = handling.prepare(image, args.wight, args.height)    # чб массив пикселей

    # перевод в ASCII-Art
    if args.set != None:
        charset = open(args.set).readline().replace("\n", "")
    else:
        charset = CHARSET

    image = converter.convert(image, charset)   # результат


    if args.output != None:
        print("out to file")
        # writer = console_writer.file_writer(args.output)
        # writer.write(image)
    else:
        writer = console_writer.ConsoleWriter()
        writer.write(image)


if __name__ == "__main__":
    main()