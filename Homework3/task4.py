# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input("Введите число:"))
t = " "
while N != 0:
    t = str(N % 2)+t
    N //= 2
print(t)
