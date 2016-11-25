import sys


def generate_unique_list(data_list):
    return_data = set()
    for i in data_list:
        return_data.add(i)

    return ','.join(sorted(return_data))


if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            num_list = line.rstrip().split(",")
            print(generate_unique_list(num_list))
