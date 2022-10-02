#5. Реализуйте алгоритм перемешивания списка.
from operator import index
from random import randint

list = [1,2,3,4,5,6,7,8]
list1=[]
for i in range (len(list)):
    index = randint( 0, len(list)-1)
    list1.append(list[index])
    list.remove(list[index])
print(list1)    
