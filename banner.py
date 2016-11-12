import sys


def banner_length(word, char="*"):
    """ Create a banner with the character the length of the word given
    :type word: String
    :type char: String """
    length = len(word)
    return char * length


def set_banner(word):
    """ Output the banner, it'll look pretty cool once it's done.
    :type word: String """
    length = banner_length(word)
    print "**{}**".format(length)
    print "* {} *".format(word)
    print "**{}**".format(length)

if __name__ == '__main__':
    set_banner(sys.argv[1])
