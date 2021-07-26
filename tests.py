import unittest

from main import choose_mode
from handlers import ReadHandler, WriteHandler


class TestAppLogic(unittest.TestCase):
    def test_choose_mode(self):
        self.assertFalse(choose_mode('log'))
        self.assertFalse(choose_mode('any_mode'))

    def test_read_file(self):
        self.assertFalse(ReadHandler('/home').read())
        self.assertFalse(ReadHandler('/home/file.txt').read())
        self.assertTrue(ReadHandler('/home/user/PycharmProjects/FilesRW/100 Sales Records.csv').read())

    def test_write_to_file(self):
        self.assertFalse(WriteHandler('/home').write())
        self.assertFalse(WriteHandler('/home/user/folder/file.txt').write())


if __name__ == '__main__':
    unittest.main()
