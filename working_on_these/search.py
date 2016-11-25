import sys


def search_string(string, key):
    """ Search a string for a specified key.
    If the key exists out put "true" if it doesn't output "false"
    >>> search_string("test", "est")
    true
    >>> search_string("testing", "rawr")
    false"""
    results = []
    for c in string:
        for ch in key:
            if c == ch:
                results.append(c)
    if len(string) / 2 < len(results) or len(string) / 2 == len(results):
        return "true"
    else:
        return "false"


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            data_list = line.rstrip().split(",")
            search_key = data_list[1]
            word = data_list[0]
            print(search_string(word, search_key))
