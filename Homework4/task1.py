# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)
from decimal import Decimal
import decimal


x = float(input("введите число x: "))
y= float(input("введите число y: "))
decimal.getcontext().prec=4   # задаем точность
a =Decimal(x)/Decimal(y)   # вычисление с заданной точностью

print(a)