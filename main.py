# -*- coding: utf-8 -*-
import exception_and_functions as eaf
from time import sleep
from os import chdir

chdir('Nie usuwać')
print('To program, który przechowuje co chcesz obejrzeć czy zrobić.')
# może dodac -> eaf.find_sth()
while 1:
    mode = input('\nWybierz listę:'
                 '\nRzeczy do zrobienia - wpisz \"1\"'
                 '\nFilmy do obejrzenia - wpisz \"2\"'
                 '\nSeriale do obejrzenia - wpisz \"3\"'
                 '\nCoś innego? Napisz do Skarba!!!'
                 '\nWybieram numer:\n')
    while 1:
        try:
            mode = int(mode)
            if 1 <= mode <= 3:
                break
            else:
                raise eaf.TooSmallOrTooBigNumber

        except ValueError:
            mode = input('Zostały wprowadzone złe dane, wpisz numer jeszcze raz\nWybieram numer: ')
            print('Sprawdzanie, czy dane wprowadzone poprawnie...')
            sleep(2)

        except eaf.TooSmallOrTooBigNumber:
            mode = input('Wprowadź numer w zakresie 1-3\nWybieram numer: ')

    choice = input('\nNapisz cyfrę:'
                   '\n1 - jeśli chcesz zobaczyć, co jest na liście'
                   '\n2 - jeśli chcesz dodać coś do listy'
                   '\n3 - jeśli chcesz usunąć coś z listy\n')
    while 1:
        try:
            choice = int(choice)
            if 1 <= choice <= 3:
                break
            else:
                raise eaf.TooSmallOrTooBigNumber

        except ValueError:
            choice = input('Zostały wprowadzone złe dane, wpisz numer jeszcze raz\nWybieram numer: ')
            print('Sprawdzanie, czy dane wprowadzone poprawnie...')
            sleep(2)

        except eaf.TooSmallOrTooBigNumber:
            choice = input('Wprowadź numer w zakresie 1-4\nWybieram numer: ')

    if choice == 1:
        if mode == 1:
            eaf.show_sth('doing.txt')
        elif mode == 2:
            eaf.show_sth('films.txt')
        elif mode == 3:
            eaf.show_sth('series.txt')

    elif choice == 2:
        List = input('\nPodaj listę rzeczy\n')
        if mode == 1:
            eaf.add_sth('doing.txt', List)
        elif mode == 2:
            eaf.add_sth('films.txt', List)
        elif mode == 3:
            eaf.add_sth('series.txt', List)

    elif choice == 3:
        if mode == 1:
            eaf.del_sth('doing.txt', eaf.del_and_try_num('doing.txt'))
        elif mode == 2:
            eaf.del_sth('films.txt', eaf.del_and_try_num('films.txt'))
        elif mode == 3:
            eaf.del_sth('series.txt', eaf.del_and_try_num('series.txt'))

    off = input('\nCzy chcesz zakończyć działanie programu? T/N\nMój wybór:\n').upper()
    if off == 'T':
        print("Program zakończył działanie")
        sleep(5)
        break
