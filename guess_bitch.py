from random import randint


def guessing_game_main():
    count = 0
    num = randint(1000, 9999)
    print num

    print """
    Welcome to the game, guess the number in as few tries
    as possible. Good luck.\n"""

    while True:
        guess = raw_input("{}> Guess the number: ".format(count))

        if int(guess) != num:
            count += 1
            print "That's not my number.."
            print "*"
        else:
            print "You did it! That took you exactly {} tries!".format(count)
            print "****"
            name = raw_input("Enter your name for the scoreboard: ")
            to_write = "Name: {}\nScore: {}\n\n".format(name, count)
            with open('score.txt', 'a') as f:
                f.write(to_write)
            return num


if __name__ == '__main__':
    guessing_game_main()