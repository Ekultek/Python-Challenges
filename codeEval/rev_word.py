import sys


def split(sentence):
    return sentence.split(" ")


def main():
    with open(sys.argv[1], "r") as words:
        for word in words.readlines():
            print ' '.join(list(reversed(split(word.rstrip()))))


if __name__ == '__main__':
    main()
