# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
from random import randint, random


N = int(input())
mult = 0
list = [randint(-N, N) for i in range(N)]
print(list)


file = open('read.txt', 'r')
for index in file:
    print(index)
    mult*= list[int(index)]
file.close()
print(mult)
