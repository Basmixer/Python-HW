# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def sum(a, b):
    if a == 0:
        return b;
    return sum(a-1, b+1)

a = int(input('Введите число (a): '))
b = int(input('Введите число (b): '))
print(sum(a, b))