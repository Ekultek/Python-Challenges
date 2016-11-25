import sys


def decode(messy_string, index):
    """ Find a famous writer and a year in a random string
    >>> print(decode("osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg",
    >>> ['3', '35', '27', '62', '51', '27', '46', '57', '26', '10', '46', '63', '57', '45', '15', '43', '53']))
    Stephen King 1947"""
    string_list = list(messy_string)
    return ''.join(string_list[int(i)-1] for i in index)


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            data_arr = line.rstrip().split("|")
            print(decode(data_arr[0], data_arr[1].strip().split(" ")))
