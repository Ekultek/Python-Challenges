def obtain_number():
    """ Get the numbers that are going to be averaged """
    arr = []
    while True:
        num = raw_input('Enter a number: ')
        arr.append(num)
        if len(arr) == 10:
            break

    return arr


def calculate_avg(numbers):
    """ Calculate the average of the numbers list """
    total = 0
    amount = len(numbers)

    for i in numbers:
        total += int(i)

    return "Average of the numbers {} is {}".format(''.join(str(numbers)), total / amount)


if __name__ == '__main__':
    arr = obtain_number()
    print calculate_avg(arr)
