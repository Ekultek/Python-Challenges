import urllib
import re


def scan_html(page):
    regex = re.compile("[0-9]")
    nums = re.findall(regex, page)
    return ''.join(nums)


def open_link(site):
    return urllib.urlopen(site)


if __name__ == '__main__':
    data = open_link("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")
    count = 0
    while True:
        with open("results.txt", "a+") as html:
            urllib.urlcleanup()
            nums = scan_html(data.read())
            data = open_link("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(nums))
            html.write("{}\n".format(nums))
            count += 1
            if count % 100 == 0:
                print count
