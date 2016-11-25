import sys
import re


def cap_words(string):
    if re.search(r"\d", string) is None:
        return string.title()
    else:
        string_list = string.split(" ")
        return string_list[0] + string_list[1].title()


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            print(cap_words(line.rstrip()))