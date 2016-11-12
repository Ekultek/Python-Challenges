import sys


if __name__ == '__main__':
    with open(sys.argv[1], "r") as numbers:
        for num in numbers:
            arr = list(num.rstrip())
            print sum(int(i) for i in arr)
