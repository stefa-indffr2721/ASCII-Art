import unittest
from console_writer import ConsoleWriter


class TestConsoleWriter(unittest.TestCase):

    def test_create(self):
        """ проверяем что ConsoleWriter создаётся без ошибок """
        writer = ConsoleWriter()
        self.assertIsNotNone(writer)

    def test_write_empty(self):
        """ проверка на то не падает ли ConsoleWriter при пустом массиве """
        writer = ConsoleWriter()
        ascii_2d = []
        try:
            writer.write(ascii_2d)
            ok = True
        except:
            ok = False
        self.assertTrue(ok)

    def test_write_multiple_rows(self):
        """ проверка не падает ли writer при вводе нескольких строк """
        writer = ConsoleWriter()
        ascii_2d = [
            [("@", 255, 0, 0), (".", 0, 255, 0)],
            [(" ", 0, 0, 255), ("#", 128, 128, 128)]
        ]
        try:
            writer.write(ascii_2d)
            ok = True
        except:
            ok = False
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()