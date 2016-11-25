import sys


def data_sum(data_list):
    return sum(data_list)


if __name__ == '__main__':
    num_data = []
    with open(sys.argv[1], "r") as data:
        for item in data.readlines():
            num_data.append(int(item.rstrip()))
    print(data_sum(num_data))
