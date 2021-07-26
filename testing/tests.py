import unittest

from handlers import TXTHandler, CSVHandler, XLSXHandler
from main import choose_mode


class TestAppLogic(unittest.TestCase):
    def test_choose_mode(self):
        self.assertFalse(choose_mode('log', '/home'))
        self.assertFalse(choose_mode('any_mode', '/home'))

    def test_read_file(self):
        # No such file testing
        self.assertFalse(TXTHandler('/home/file123.txt').read())
        self.assertFalse(CSVHandler('/home/file123.txt').read())
        self.assertFalse(XLSXHandler('/home/file123.txt').read())

        # Directory as file path testing
        self.assertFalse(TXTHandler('/home').read())
        self.assertFalse(CSVHandler('/home').read())
        self.assertFalse(XLSXHandler('/home').read())

        # Empty TXT file opening test
        self.assertFalse(TXTHandler('/home/user/PycharmProjects/FilesRW/testing/empty.txt').read())
        # Non empty TXT file opening test(only 3 lines)
        self.assertTrue(TXTHandler('/home/user/PycharmProjects/FilesRW/testing/file1.txt').read())

        # Empty CSV file opening test
        self.assertFalse(CSVHandler('/home/user/PycharmProjects/FilesRW/testing/empty.csv').read())
        # Non empty CSV file opening test
        self.assertTrue(CSVHandler('/home/user/PycharmProjects/FilesRW/testing/100 Sales Records.csv').read())

        # Empty XLSX file opening test
        self.assertFalse(XLSXHandler('/home/user/PycharmProjects/FilesRW/testing/empty.xlsx').read())
        # Non empty XLSX file opening test
        self.assertTrue(XLSXHandler('/home/user/PycharmProjects/FilesRW/testing/test.xlsx').read())

    def test_write_to_file(self):
        # No permissions test
        self.assertFalse(TXTHandler('home/file.txt').write())
        self.assertFalse(CSVHandler('home/file.txt').write())
        self.assertFalse(XLSXHandler('home/file.txt').write())

        # No such file test
        self.assertFalse(TXTHandler('/home/user/folder/empty.txt').write())
        self.assertFalse(CSVHandler('/home/user/folder/empty.txt').write())
        self.assertFalse(XLSXHandler('/home/user/folder/empty.txt').write())


if __name__ == '__main__':
    unittest.main()
