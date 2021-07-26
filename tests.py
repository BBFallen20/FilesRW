import unittest

from main import choose_mode
from handlers import TXTHandler, CSVHandler, XLSXHandler


class TestAppLogic(unittest.TestCase):
    def test_choose_mode(self):
        self.assertFalse(choose_mode('log', '/home'))
        self.assertFalse(choose_mode('any_mode', '/home'))

    def test_read_file(self):
        self.assertFalse(TXTHandler('/home/file123.txt').read())
        self.assertFalse(CSVHandler('/home/file123.txt').read())
        self.assertFalse(XLSXHandler('/home/file123.txt').read())
        self.assertTrue(TXTHandler('/home/user/PycharmProjects/FilesRW/file.txt').read())
        self.assertTrue(CSVHandler('/home/user/PycharmProjects/FilesRW/100 Sales Records.csv').read())
        self.assertTrue(XLSXHandler('/home/user/PycharmProjects/FilesRW/test.xlsx').read())

    def test_write_to_file(self):
        self.assertFalse(TXTHandler('/home/user/folder/file.txt').write())
        self.assertFalse(CSVHandler('/home/user/folder/file.txt').write())
        self.assertFalse(XLSXHandler('/home/user/folder/file.txt').write())


if __name__ == '__main__':
    unittest.main()
