# <~~ coding=utf-8 ~~>
import argparse


opts = argparse.ArgumentParser()
opts.add_argument("-g", "--greek", type=int,
                  help="Convert to Medieval Numerals")
opts.add_argument("-r", "--roman", type=int,
                  help="Convert to Roman Numerals")
args = opts.parse_args()


ROMAN_NUMERAL_TABLE = (
    ("~M", 1000000), ("~D", 500000), ("~C", 100000),
    ("~L", 50000), ("~X", 10000), ("~V", 5000),  # "~" indicates a Macron
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
)


GREEK_NUMERAL_TABLE = (
    ("α", 1), ("β", 2), ("γ", 3),
    ("δ", 4), ("ε", 5), ("Ϝ", 6),
    ("ζ", 7), ("η", 8), ("θ", 9),
    ("ι", 10), ("κ", 20), ("λ", 30),
    ("μ", 40), ("ν", 50), ("ξ", 60),
    ("ο", 70), ("π", 80), ("ϙ", 90),
    ("ρ", 100), ("σ", 200), ("τ", 300),
    ("υ", 400), ("φ", 500), ("χ", 600),
    ("ψ", 700), ("ω", 800), ("ϡ", 900),
    ("α", 1000), ("β", 2000), ("γ", 3000),
    ("δ", 4000), ("ε", 5000), ("ϛ", 6000),
    ("ζ", 7000), ("η", 8000), ("θ", 9000)  # The Greeks weren't very creative
)


def convert_init(number, convert_to=None):
    """ Convert a number to a numeral, Greek or Roman
    >>> print(convert_init(45, convert_to=GREEK_NUMERAL_TABLE))
    ϜϜϜϜϜϜϜγ
    >>> print(convert_init(45, convert_to=ROMAN_NUMERAL_TABLE))
    XLV """
    display_numerals = []

    for numeral, value in sorted(convert_to)[::-1]:  # sort the list from largest to least
        count = number // value
        number -= count * value
        display_numerals.append(numeral * count)

    return ''.join(display_numerals)


if __name__ == '__main__':
    if args.greek:
        data = convert_init(int(args.greek), convert_to=GREEK_NUMERAL_TABLE)
        with open("greek_numerals.txt", "a+") as file_data:
            file_data.write(data)  # Write it to a file

    elif args.roman:
        data = convert_init(int(args.roman), convert_to=ROMAN_NUMERAL_TABLE)
        with open("roman_numerals.txt", "a+") as file_data:
            file_data.write(data)

    else:
        raise NotImplementedError("{} is not implemented yet".format(args))
