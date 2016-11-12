import itertools


def split_string(string):
    return list(string)


def _mutate_element(elements):
    return itertools.permutations(elements, len(elements))


def main(string):
    arr = split_string(string)
    return list(_mutate_element(arr))


if __name__ == '__main__':
    data = []
    with open("challenge_strings.txt", "r") as strings:
        for string in strings.readlines():
            data.append(main(string.rstrip()))

    for item in data:
        print "There are a total of: {} ways to permutate the string".format(len(item))
