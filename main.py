

def read_file(file_path: str) -> bool:
    try:
        with open(file_path, 'r') as File:
            if len(File.readline(1)) > 0:
                print('Here is first lines from the file:\n')
                [print(line) for line in File.readlines()[:5]]
                return True
            print('File is empty.')
    except FileNotFoundError:
        print('File not found.')
    except PermissionError:
        print('You don`t have permission to use this file.')
    except IsADirectoryError:
        print('Path is a directory.')
    return False


def write_to_file(file_path: str) -> bool:
    try:
        with open(file_path, 'a') as File:
            File.writelines([input('Enter line:\n')+'\n' for _ in range(int(input('Enter lines amount:\n')))])
        print('File extended successfully.')
        return True
    except FileNotFoundError:
        print('File not found.')
    except PermissionError:
        print('You don`t have permission to use this file.')
    except ValueError:
        print('Enter digit for lines amount.')
    except IsADirectoryError:
        print('Path is a directory.')
    return False


def choose_mode(mode: str) -> bool:
    modes = {'read': read_file, 'write': write_to_file}
    completed = False
    if mode in modes:
        completed = modes[mode](input('Enter file path:\n'))
    else:
        print('Error. Mode does not exist.')
    return completed


if __name__ == '__main__':
    print(f'{"= " *10} Choose mode {"= " *10}')
    selected_mode = input('Read: read file mode;\n''Write: write to file mode.\n').lower()
    choose_mode(selected_mode)
