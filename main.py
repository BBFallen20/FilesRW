import argparse
from handlers import ReadHandler, WriteHandler


def choose_mode(mode: str) -> bool:
    modes = {'read': ReadHandler, 'write': WriteHandler}
    completed = False
    if mode == 'read':
        completed = modes[mode](input('Enter file path:\n')).read()
    elif mode == 'write':
        completed = modes[mode](input('Enter file path:\n')).write()
    else:
        print('Error. Mode does not exist.')
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
    choose_mode(selected_mode)
