import unittest

from main import choose_mode, read_mode, write_mode


class TestAppLogic(unittest.TestCase):
    def test_choose_mode(self):
        self.assertFalse(choose_mode('log'))
        self.assertFalse(choose_mode('any_mode'))

    def test_read_file(self):
        self.assertFalse(read_mode('/home'))
        self.assertFalse(read_mode('/home/file.txt'))
        self.assertTrue(read_mode('/home/user/PycharmProjects/FilesRW/100 Sales Records.csv'))

    def test_write_to_file(self):
        self.assertFalse(write_mode('/home'))
        self.assertFalse(write_mode('/home/user/folder/file.txt'))


if __name__ == '__main__':
    unittest.main()
