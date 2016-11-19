import json
import sys


def calc_sum(json_data):
    return sum(item.get('id', 0) for item in json_data['menu']['items'] if item and 'label' in item)

if __name__ == '__main__':
    with open(sys.argv[1], "r") as data:
        data = json.load(data)
        print(calc_sum(data))
