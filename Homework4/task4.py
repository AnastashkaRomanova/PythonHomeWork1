# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint, choice


lst= [int(randint(1,100)) for k in range( 1,101)]


def get_polynomial(list, degree_k):
    items = ['+', '-']
    with open('filetask4.txt','a', encoding='utf-8') as my_file:
        for i in list:
            if i > 0 and degree_k > 0:
                my_file.write(f' {i}*x^{degree_k} ')
                my_file.write(choice(items))
                degree_k -= 1
        if list[i] != 0:        
            my_file.write(f" {list[i]} = 0 \n")
            my_file.close()

degree_k = int(input('Введите число: '))

get_polynomial(lst, degree_k)
