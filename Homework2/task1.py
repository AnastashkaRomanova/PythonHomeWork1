# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


N = (input("Введите число: "))
sum = 0
for i in str(N):
    if i !="." and i!=",":
        sum = sum + int(i)
print(sum)        





