# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

xA = float(input("Введите координату X точки A: "))
yA = float(input("Введите координату Y точки A: "))
xB = float(input("Введите координату X точки B: "))
yB = float(input("Введите координату X точки B: "))

length = round((((xA-xB)**2+(yA-yB)**2)**0.5), 2)
# length = int(length * 100) / 100

print(length)