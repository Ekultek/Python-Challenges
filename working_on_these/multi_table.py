if __name__ == '__main__':
    for row in range(1, 20+1):
        table = ''
        for column in range(1, 20+1):
            table += '{:<4} '.format(row * column)
        print(table)