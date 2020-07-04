class TooSmallOrTooBigNumber(Exception):
    pass


def show_sth(name_of_file: str):
    with open(name_of_file, encoding='utf-8') as file:
        for line in range(1, number_of_elements(name_of_file) + 1):
            print('{}. {}'.format(line, file.readline()))


def number_of_elements(name_of_file: str):
    with open(name_of_file, encoding='utf-8') as file:
        elements_in_file = len(file.read().split('\n'))
        return elements_in_file


def add_sth(nameoffile: str, things: str):
    temp, j, things = things.split(','), 0, []
    print(temp)
    print(things)
    things = [thing.strip() for thing in temp]

    with open(nameoffile, 'a', encoding='utf-8') as file:
        for element in range(len(things)):
            j += 1
            file.write(things[element])
            if len(things) != j:
                file.write('\n')


def find_sth(name_of_file: str, integer: int):
    pass


def del_sth(name_of_file: str, number: int):
    with open(name_of_file, 'r', encoding='utf-8') as file:
        iterator, j, temp = 0, 0, []
        for row in file:
            iterator += 1
            if iterator != number:
                temp.append(row)
        number_of_elements_in_file = number_of_elements(name_of_file)

    with open(name_of_file, 'w', encoding='utf-8') as file:
        for row in temp:
            j += 1
            if j != number_of_elements_in_file:
                print(row, file=file, end='')
            else:
                row.replace('\n', '')
                print(row, file=file, end='')


def del_and_try_num(name_of_file: str):
    from time import sleep
    num = input('\nPodaj pozycje, którą chcesz usunąć\n')
    while 1:
        try:
            num = int(num)
            if 1 <= num <= number_of_elements(name_of_file):
                break
            else:
                raise TooSmallOrTooBigNumber
        except ValueError:
            num = input('Zostały wprowadzone złe dane, wpisz numer jeszcze raz\nWybieram numer:\n')
            print('Sprawdzanie, czy dane wprowadzone poprawnie...')
            sleep(2)
        except TooSmallOrTooBigNumber:
            num = input('Wprowadź numer w zakresie 1-{}\nWybieram numer:'
                        '\n'.format(number_of_elements(name_of_file)))
    return num


def change_sth():
    pass
