import sys


def remove_dupes(arr):
    res = set()
    for i in arr:
        if i not in res:
            res.add(i)
    return res


if __name__ == '__main__':
    with open(sys.argv[1], "r") as numbers:
        for i in numbers.readlines():
            remove_dupes(int(numbers.rstrip().split(",")))
