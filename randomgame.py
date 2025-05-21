import random

def declension(n):
    if n % 10 == 1 and n % 100 != 11:
        return 'попытка'
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return 'попытки'
    else:
        return 'попыток'

def saferesult(f, d):
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{f}: {d} {declension(d)}")

print('Я загадал число от 0 до 100 сможешь ли ты его угадать?')

while True:
    print('Выберите действие:')
    print('1 - играть в угадай число')
    print('2 - посмотреть рекорды')
    print('3 - выйти из игры')

    m = int(input())

    if m == 1:
        print('Скажи своё имя путник.')
        f = input()
        print('Говори число, я годов!!!')
        d = 0
        s = random.randint(0, 100)
        while True:
            d = d + 1
            a = int(input())
            if a > s:
                print(f'{d} {declension(d)}. Заданное число меньше, попробуйте ещё раз:')
            elif a < s:
                print(f'{d} {declension(d)}. Заданное число больше, попробуйте ещё раз:')
            else:
                print(f'{d} {declension(d)}. ПОБЭДАААААААААААААА!!!!!!')
                saferesult(f, d)
                print('Сыграем ещё раз?')
                print('1 - да')
                print('2 - нет')
                v = int(input())
                if v == 1:
                    break
                elif v == 2:
                    print('Возвращайся ещё :3')
                    exit()
                else:
                    print('Я не понимаю чего ты хочешь человечишка')

    elif m == 2:
        with open('result.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    
    elif m == 3:
        print('Возвращайся ещё :3')
        exit()
    
    else:
        print('Я не понимаю чего ты хочешь человечишка')
