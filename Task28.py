#Задача 28: Напишите рекурсивную функцию sum(a, b), 
#возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#*Пример:*
#2 2
#    4 
print("Нужно ввести целые, неотрицателные числа")
number_a = int(input("Введите число a:  "))
number_b = int(input("Введите число b:  "))
def number_sum(number_a, number_b):
    if number_a == 0:
        return number_b
    else:    
        return number_sum(number_a - 1, number_b + 1)
print(number_sum(number_a, number_b))