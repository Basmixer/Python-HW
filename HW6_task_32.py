# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_custom = [4, 6, 67, 77, 34, 456, 7, 879, 6, 3, 2, 1, 90, 98, 4, 7, 88, 6, 43, 3]
min_number = int(input('введите минимальное значение диапазона: '))
max_number = int(input('введите максимальное значение диапазона: '))
for i in range(len(list_custom)):
    if min_number <= list_custom[i] <= max_number:
        print(i)
        
