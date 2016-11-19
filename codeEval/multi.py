import sys


def multiply(x, y):
    max_multiple_try = 0
    while max_multiple_try != float("inf"):
        res = x * max_multiple_try
        if res != x and res >= y:
            return res
        else:
            max_multiple_try += 1


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            numbers = line.rstrip().split(",")
            print(multiply(int(numbers[1]), int(numbers[0])))
