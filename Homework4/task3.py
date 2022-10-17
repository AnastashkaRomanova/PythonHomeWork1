# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint, random

N = int(input('Введите количество чисел в списке:'))

new_list = []

def get_list(list):
    for k in range(N):
        list.append(randint(1, 20))
    print(list)


def unique_list(list):
    unique = []
    for i in list:
        if i in unique:
            i+=1
        else:
            unique.append(i)   
    return unique     
               
get_list(new_list)
print(unique_list(new_list))        
        
        
          


unique_list(new_list)