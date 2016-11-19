import sys


def find_smallest_multiple_of_two(x, n):
    """ Find the smallest multiple of given number n that is greater than x
    >>> print(find_smallest_multiple_of_two(13, 8))
    16
    >>> print(find_smallest_multiple_of_two(28, 4))
    32 """
    to_multiply = n
    while to_multiply < x:
        to_multiply <<= 1
    return to_multiply


def find_difference_between_bits(x, n):
    """ Find the bit difference between x and n
    >>> print(find_difference_between_bits(13, 8))
    10
    >>> print(find_difference_between_bits(28, 4))
    13 """
    binary_x = int(bin(x)[2:])
    binary_n = int(bin(n)[2:])
    diff = binary_x ^ binary_n
    return diff.bit_length()-1


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            x, n = line.rstrip().split(",")
            print("Smallest multiple: {}".format(find_smallest_multiple_of_two(int(x), int(n))))
            print("Bit difference: {}".format(find_difference_between_bits(int(x), int(n))))
