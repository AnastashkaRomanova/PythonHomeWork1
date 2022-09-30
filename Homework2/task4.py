# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
from random import randint, random


N = int(input())
list = [randint(-N, N) for i in range(-N, N+1)]
print(list)

indexs = 'file.txt'
file = open(indexs, 'r')
for index in file:

    print(index)
file.close()
