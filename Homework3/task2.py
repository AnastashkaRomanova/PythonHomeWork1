# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

N = int(input('Введите количество чисел в списке:'))

new_list = []


def get_list(list):
    for k in range(N):
        list.append(randint(1, 10))
    print(list)


def pow_method(list):
    pow = 0
    l = len(list)//2
    if len(list) % 2 != 0:
        l = len(list)//2+1
    for i in range(l):
        pow = list[i]*list[len(list)-i-1]
        print(pow)


get_list(new_list)
pow_method(new_list)
