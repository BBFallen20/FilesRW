import unittest

from handlers import TXTHandler, CSVHandler, XLSXHandler, ExtensionHandler
from main import choose_mode


class TestAppLogic(unittest.TestCase):
    def test_choose_mode(self):
        self.assertFalse(choose_mode('log', '/home'))
        self.assertFalse(choose_mode('any_mode', '/home'))

    def test_TXTHandler(self):
        # Read method testing

        # No such file testing
        self.assertFalse(TXTHandler('/home/file123.txt').read())
        # Directory as file path testing
        self.assertFalse(TXTHandler('/home').read())
        # Empty TXT file opening test
        self.assertFalse(TXTHandler('/home/user/PycharmProjects/FilesRW/testing/files/empty.txt').read())
        # Non empty TXT file opening test(only 3 lines)
        self.assertTrue(TXTHandler('/home/user/PycharmProjects/FilesRW/testing/files/file1.txt').read())

        # Write method test

        # No permissions test
        self.assertFalse(TXTHandler('home/file.txt').write())
        # No such file test
        self.assertFalse(TXTHandler('/home/user/folder/empty.txt').write())

    def test_CSVHandler(self):
        # Read method testing

        # No such file testing
        self.assertFalse(CSVHandler('/home/file123.txt').read())
        # Directory as file path testing
        self.assertFalse(CSVHandler('/home').read())
        # Empty CSV file opening test
        self.assertFalse(CSVHandler('/home/user/PycharmProjects/FilesRW/testing/files/empty.csv').read())
        # Non empty CSV file opening test
        self.assertTrue(CSVHandler('/home/user/PycharmProjects/FilesRW/testing/files/100 Sales Records.csv').read())

        # Write method testing

        # No permissions test
        self.assertFalse(CSVHandler('home/file.txt').write())
        # No such file test
        self.assertFalse(CSVHandler('/home/user/folder/empty.txt').write())

    def test_XLSXHandler(self):
        # Read method testing

        # No such file testing
        self.assertFalse(XLSXHandler('/home/file123.txt').read())
        # Directory as file path testing
        self.assertFalse(XLSXHandler('/home').read())
        # Empty XLSX file opening test
        self.assertFalse(XLSXHandler('/home/user/PycharmProjects/FilesRW/testing/files/empty.xlsx').read())
        # Non empty XLSX file opening test
        self.assertTrue(XLSXHandler('/home/user/PycharmProjects/FilesRW/testing/files/test.xlsx').read())

        # Write method testing

        # No permissions test
        self.assertFalse(XLSXHandler('home/file.txt').write())
        # No such file test
        self.assertFalse(XLSXHandler('/home/user/folder/empty.txt').write())

    def test_ExtensionHandler_error_wrapper(self):
        wrapper = ExtensionHandler.error_wrapper
        # No such file
        self.assert_(wrapper(TXTHandler('/home/user/folder/empty.txt').read()))
        # Empty file reading
        self.assert_(wrapper(TXTHandler('/home/user/PycharmProjects/FilesRW/testing/files/empty.txt').read()))
        # Directory as a path
        self.assert_(wrapper(TXTHandler('/home/user/folder').read()))


if __name__ == '__main__':
    unittest.main()
