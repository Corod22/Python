#Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8
number_a = int(input("Введите число a:  "))
number_b = int(input("Введите число b:  "))
def func(number_a, number_b):
    if number_b == 0:
        return 1
    return number_a * func(number_a, number_b - 1)
print(func(number_a, number_b))