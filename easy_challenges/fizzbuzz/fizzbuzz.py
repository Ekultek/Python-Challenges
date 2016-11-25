import sys


def fizzbuzz(num_range, div_low=3, div_high=5):
    series = []
    for x in num_range:
        if x % div_low == 0 and x % div_high == 0:
            series.append("FB")
        elif x % div_low == 0:
            series.append("F")
        elif x % div_high == 0:
            series.append("B")
        else:
            series.append(str(x))

    return ' '.join(series)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as nums:
        for num in nums.readlines():
            num_arr = num.rstrip().split(" ")
            low = int(num_arr[0])
            high = int(num_arr[1])
            num_range = range(1, int(num_arr[2]) + 1)
            print(fizzbuzz(num_range, div_low=low, div_high=high))
