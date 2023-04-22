# Задача 26:  Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def high_a_in_b(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / high_a_in_b(a, -b)
    if b % 2 == 0:
        return high_a_in_b(a, b // 2) * high_a_in_b(a, b // 2)
    else:
        return high_a_in_b(a, b - 1) * a

a = int(input('Введите число (a), которое будет возведено в степень: '))
b = int(input('Введите число, соответствующее степени (b): '))
print(high_a_in_b(a, b))