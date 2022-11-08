# 1. Задайте строку из набора чисел.
#  Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

str = "1 5 87 9 46 23 47 21 12"


# list = str.split()
# for i in range(len(list)):
#     list[i]= int (list[i])
# print(list)
# print( max(list), min(list) )    

str = "1 5 87 9 46 23 47 21 12".split()
lst= list((map(int, str)))
print(max(lst), min(lst))