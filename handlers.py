import csv
from abc import abstractmethod, ABC
from typing import Callable

import openpyxl
import xlsxwriter


class ExtensionHandler(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @staticmethod
    def error_wrapper(func) -> bool or Callable:
        def outer(self) -> bool or Callable:
            try:
                return func(self)
            except FileNotFoundError:
                print('File not found.')
            except PermissionError:
                print('You don`t have permission to use this file.')
            except ValueError:
                print('Enter digit for lines amount.')
            except IsADirectoryError:
                print('Path is a directory.')
            return False
        return outer


class CSVHandler(ExtensionHandler):
    @ExtensionHandler.error_wrapper
    def read(self):
        with open(self.file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            counter = 0
            for row in reader:
                print(row)
                counter += 1
                if counter == 5:
                    break
        return True

    @ExtensionHandler.error_wrapper
    def write(self):
        with open(self.file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([input('Enter line:\n') + ';' for _ in range(int(input('Enter lines amount:\n')))])
        print('File extended successfully.')
        return True


class TXTHandler(ExtensionHandler):
    @ExtensionHandler.error_wrapper
    def read(self):
        with open(self.file_path, 'r') as File:
            if len(File.readline(1)) > 0:
                print('Here is first lines from the file:\n')
                [print(line) for line in File.readlines()[:5]]
                return True
            print('File is empty.')
            return False

    @ExtensionHandler.error_wrapper
    def write(self):
        with open(self.file_path, 'a') as File:
            File.writelines([input('Enter line:\n') + '\n' for _ in range(int(input('Enter lines amount:\n')))])
        print('File extended successfully.')
        return True


class XLSXHandler(ExtensionHandler):
    @ExtensionHandler.error_wrapper
    def read(self):
        with open(self.file_path, 'r') as File:
            wb_obj = openpyxl.load_workbook(self.file_path)
        sheet = wb_obj.active
        for row in sheet.iter_rows(max_row=5):
            for cell in row:
                print(cell.value, end=" ")
            print()
        return True

    @ExtensionHandler.error_wrapper
    def write(self):
        with open(self.file_path, 'r') as File:
            workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet('test')
        data_list = [input('Enter column:\n') for _ in range(int(input('Enter columns amount:\n')))]
        for col_num, data in enumerate(data_list):
            worksheet.write(0, col_num, data)
        workbook.close()
        print('File extended successfully.')
        return True

