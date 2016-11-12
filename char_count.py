def split_words(data):
    arr = []
    for char in data:
        if char != "\n":
            arr.append(char)
    return arr


def append_to_hash(data, word_hash):
    for word in data:
        if word in word_hash:
            word_hash[word] += 1
        else:
            word_hash[word] = 1

    return word_hash


if __name__ == '__main__':
    word_dict = {}
    count = 0

    with open("story.txt", "r") as story:
        data = story.read()
        word_arr = split_words(data.strip())
        append_to_hash(word_arr, word_dict)
        for x in word_dict.values():
            count += x

    print "Total characters in file: {}".format(count)
