import argparse
from handlers import CSVHandler, TXTHandler, XLSXHandler, ExtensionHandler


def choose_mode(mode: str, file_path: str) -> bool:
    file_extension = file_path.split('.')[-1] if file_path.__contains__('.') else ''
    completed = False
    extensions = {
        'txt': TXTHandler,
        'csv': CSVHandler,
        'xlsx': XLSXHandler,
        'xls': CSVHandler
    }
    extension_found = extensions.get(file_extension)
    if extension_found and mode == 'write' or mode == 'read':
        extension_found(file_path).write() if mode == 'write' else extension_found(file_path).read()
    else:
        print('Unknown file extension or mode. ')
    return completed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Application mode(write/read) selector')
    parser.add_argument(
        'mode',
        metavar='mode',
        type=str,
        help='application mode'
    )
    parser.add_argument(
        'path',
        metavar='path',
        type=str,
        help='file path'
    )
    args = parser.parse_args()
    selected_mode = args.mode.lower()
    path = args.path
    choose_mode(selected_mode, path)
