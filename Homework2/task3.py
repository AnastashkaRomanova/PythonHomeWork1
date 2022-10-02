# 3. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму (округляйте до 3 знаков после запятой).

# Пример:

# - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
# Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)

from re import I


N= int (input())
list= []
for i in range(1, N+1):
    list.append(round((1+ 1/i)**i, 3))
    i+=1
print(list)
def summ_number(numbers):
    sum=0
    for num in numbers:
        sum= sum+num
        num+=1
    return sum    
print(summ_number(list))    

  


