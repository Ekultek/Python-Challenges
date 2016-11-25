import sys


def longest_sequence(compare, compare_against):
    compare_list = list(compare)
    compare_against_list = list(compare_against)
    found_list = []

    for char in compare_against_list:
        if char in compare_list and char not in found_list:
            found_list.append(char)

    return ''.join(found_list)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as data:
        for char in data.readlines():
            sequences = char.split(";")
            print(longest_sequence(sequences[0], sequences[1]))
