# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#     Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет


# day_number = int(input("Введите день недели от 1 до 7: "))
# if (day_number < 6 and day_number > 1):
#     print("это рабочий день")

# if (day_number > 5 and day_number < 8):
#     print("это выходной день!")

# if (day_number > 7 and day_number < 1):
#     print("нет такого дня недели")

day_number = int(input("Введите день недели от 1 до 7: "))

if(0<day_number <6):
    print("нет")
elif 8 > day_number > 5:
    print("да")
else:
    print("нет такого дня недели")
