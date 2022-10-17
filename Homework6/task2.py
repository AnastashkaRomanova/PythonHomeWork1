# 2. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [1, 30, 8, 9, 4, 15, 4, 55]
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum = sum + list[i]
# print(sum)

from functools import reduce


lst = [1, 30, 8, 10, 4, 15, 4, 50]
print(reduce(lambda x, y: x+y , [lst[i] for i in range(len(lst)) if i % 2 != 0]))

# lst1 = [lst[i] for i in range(len(lst)) if i % 2 != 0]
# print(lst1)
# print(sum(lst1))


#первый вариант кода:

# list = [1, 30, 8, 9, 4, 15, 4, 55]
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum = sum + list[i]
# print(sum)