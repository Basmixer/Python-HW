# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

def nearest_value(lst, target):
    return min(lst, key = lambda x: abs(x - target))

number = int(input('Введите натуральное число (N): '))
print(f'{number} - задано такое количество элементов массива')

spisok = []
for i in range(number):
    i += 1
    spisok.append(i)

print(spisok)
desired_number = int(input('Введите число (X), к которому будем искать ближайшее из массива: '))

print(desired_number)
print(f'-> {nearest_value(spisok, desired_number)}')
