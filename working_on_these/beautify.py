import string
import sys


BEAUTIFICATION = {
    "a": 24, "b": 25, "c": 26,
    "d": 1, "e": 2, "f": 3,
    "g": 4, "h": 5, "i": 6,
    "j": 7, "k": 8, "l": 9,
    "m": 10, "n": 11, "o": 12,
    "p": 13, "q": 14, "r": 15,
    "s": 16, "t": 17, "u": 18,
    "v": 19, "w": 20, "x": 21,
    "y": 22, "z": 23,
}


def strip_string(start_string):
    exclude = set(string.punctuation)
    new_string = ''.join(ch for ch in start_string if ch not in exclude)
    return new_string.replace(" ", "")


def calculate_sum(beautiful_string):
    total = []
    for c in beautiful_string.lower():
        total.append(BEAUTIFICATION[c])
    return sum(total)


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for strings in data.readlines():
            use_string = strip_string(strings.strip())
            print(calculate_sum(use_string))
