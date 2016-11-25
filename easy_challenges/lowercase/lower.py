import sys


if __name__ == '__main__':
    with open(sys.argv[1], "r") as strings:
        for string in strings:
            print string.lower()