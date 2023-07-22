def main_while():
    number = int(input('Give a number:\n'))
    while number != 0:
        if number > 0:
            print(number * number)
        elif number < 0:
            print('Unsuitable number')
        number = int(input('Give a number:\n'))


def main_break():
    while True:
        number = int(input('Give a number:\n'))
        if number > 0:
            print(number * number)
        elif number == 0:
            break
        else:
            print('Unsuitable number')


def main_continue():
    number = 1
    while number != 0:
        number = int(input('Give a number:\n'))
        if number > 0:
            print(number * number)
        elif number == 0:
            continue
        else:
            print('Unsuitable number')




if __name__ == '__main__':
    main_while()
    main_break()
    main_continue()
