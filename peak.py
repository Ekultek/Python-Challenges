import pickle
import urllib


def open_site(site):
    return urllib.urlopen(site)


def handle_image(data):
    return pickle.load(data)


if __name__ == '__main__':
    data = open_site("http://www.pythonchallenge.com/pc/def/banner.p")
    info = handle_image(data)
    for c in info:
        print ''.join(e[1] * e[0] for e in c)