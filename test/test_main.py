import unittest
import os
import main


class FakeArgs:
    set = None


class TestGetCharset(unittest.TestCase):

    def setUp(self):
        self.temp_file = "temp_charset_test.txt"

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_default(self):
        """ если файл с символами не указан, то возвращаем CHARSET """
        args = FakeArgs()
        args.set = None
        result = main.get_charset(args)
        self.assertEqual(result, main.CHARSET)

    def test_from_file(self):
        """ если файл с символами указан, то берем CHARSET из него"""
        with open(self.temp_file, "w") as f:
            f.write(" @\n")
        args = FakeArgs()
        args.set = self.temp_file
        result = main.get_charset(args)
        self.assertEqual(result, " @")

    def test_empty_file(self):
        """ если файл с набором символов пуст, то завершаем программу с ошибкой """
        with open(self.temp_file, "w") as f:
            f.write("")
        args = FakeArgs()
        args.set = self.temp_file
        with self.assertRaises(SystemExit):
            main.get_charset(args)


if __name__ == "__main__":
    unittest.main()