#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no
print("Введите первую длину шоколадки из долек ")
n=int(input())
print("Введите вторую длину щоколадки из долек")
m=int(input())
print("Введите сколько долек хотите отломить от шоколадки ")
k = int(input())
if k%n == 0 or k%m == 0:
    print('можно отломить')
else: print('Отломить нельзя')
