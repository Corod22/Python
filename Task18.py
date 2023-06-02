#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint
n=int(input('Введите количество элементорв списка: '))
list_1=[]
for i in range(n):
    n1=randint(0,10)
    list_1.append(n1)
print(list_1)
list_n = list(map(int, list_1))
x = int (input('Введите число х: '))
def nearval(list_n, number):
    return min(list_n, key=lambda x: abs(number - abs(x))) 
print(f'Ближайшее к {x} число в массиве: {nearval(list_n, x)}')