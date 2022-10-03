# 3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform
N = int(input('Введите количество чисел в списке:'))

new_list = []
droblist = []


def get_list(list):
    for k in range(N):
        list.append(round((uniform(1, 10)), 2))
    print(list)


def diff_max_min(list):
    max = list[0]
    min = list[1]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return max-min


get_list(new_list)
for i in range(len(new_list)):
    droblist.append(round((new_list[i] % 1), 2))
print(droblist)
print(
    f'Разность максимального и минимального значений дробной части элементов :  {round(diff_max_min(droblist), 2)}')
