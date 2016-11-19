import os
import sys


def get_file_size(filename):
    return os.path.getsize(filename)


if __name__ == '__main__':
    print(get_file_size(sys.argv[1]))
