import sys
import itertools


def find_permutations(word):
    for p in itertools.permutations(word):
        yield p


if __name__ == '__main__':
    results = []
    with open(sys.argv[1]) as data:
        for line in data.readlines():
            for perm in find_permutations(line.rstrip()):
                permstr = ''.join(perm)
                results.append(permstr)

    print(','.join(results))
