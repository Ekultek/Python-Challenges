import sys


def nums_to_words(number):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety']
    thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
                 'quintillion', 'sextillion', 'septillion', 'octillion',
                 'nonillion', 'decillion', 'undecillion', 'duodecillion',
                 'tredecillion', 'quattuordecillion', 'sexdecillion',
                 'septendecillion', 'octodecillion', 'novemdecillion',
                 'vigintillion']
    words = []

    if number == 0:
        words.append("zero")
    else:
        number_string = "%d" % number
        length_of_number_string = len(number_string)
        number_groups = (length_of_number_string + 2) / 3
        new_number_string = number_string.zfill(number_groups * 3)
        for i in range(0, number_groups * 3, 3):
            x, y, z = int(new_number_string[i]), int(new_number_string[i + 1]), int(new_number_string[i + 2])
            w = number_groups - (i / 3 + 1)
            if x >= 1:
                words.append(units[x])
                words.append("hundred")
            if y > 1:
                words.append(tens[y])
                if z >= 1:
                    words.append(units[z])
            elif y == 1:
                if z >= 1:
                    words.append(teens[z])
                else:
                    words.append(tens[y])
            else:
                if z >= 1:
                    words.append(units[z])
            if (w >= 1) and ((x + y + z) > 0):
                words.append(thousands[w])

    name = []

    for word in words:
        name.append(word.title())

    return ''.join(name) + "Dollars"


if __name__ == '__main__':
    with open(sys.argv[1], "r") as numbers:
        for num in numbers.readlines():
            print(nums_to_words(int(num)))
