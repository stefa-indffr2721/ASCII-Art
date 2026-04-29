import unittest
import converter


class TestConverter(unittest.TestCase):

    def test_black(self):
        """ чёрный пиксель должен давать первый символ из CHARSET """
        pixels_2d = [[(0, 0, 0, 0)]]
        charset = " .+*=#@"
        result = converter.convert(pixels_2d, charset)
        self.assertEqual(result[0][0][0], " ")

    def test_white(self):
        """ белый пиксель должен давать последний символ из CHARSET """
        pixels_2d = [[(255, 255, 255, 255)]]
        charset = " .+*=#@"
        result = converter.convert(pixels_2d, charset)
        self.assertEqual(result[0][0][0], "@")

    def test_size(self):
        """ входной и выходной массивы должны иметь одинаковый размер """
        pixels_2d = [
            [(0, 0, 0, 0), (128, 128, 128, 128), (255, 255, 255, 255)],
            [(64, 64, 64, 64), (192, 192, 192, 192), (32, 32, 32, 32)]
        ]
        charset = " .+*=#@"
        result = converter.convert(pixels_2d, charset)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 3)

if __name__ == "__main__":
    unittest.main()