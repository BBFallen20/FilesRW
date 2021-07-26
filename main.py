import argparse
from handlers import CSVHandler, TXTHandler, XLSXHandler


def choose_mode(mode: str, file_path: str) -> bool:
    file_extension = file_path.split('.')[-1] if file_path.__contains__('.') else ''
    completed = False
    extensions = {
        'txt': TXTHandler,
        'csv': CSVHandler,
        'xlsx': XLSXHandler,
        'xls': CSVHandler
    }
    if file_extension in extensions:
        if mode == 'read':
            completed = extensions[file_extension](file_path).read()
        elif mode == 'write':
            completed = extensions[file_extension](file_path).write()
        else:
            print('Unknown mode')
    else:
        print('Unknown file extension.')
    return completed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Application mode(write/read) selector')
    parser.add_argument(
        'mode',
        metavar='mode',
        type=str,
        help='application mode'
    )
    args = parser.parse_args()
    selected_mode = args.mode.lower()
    path = input('Enter file path(full):\n')
    choose_mode(selected_mode, path)
