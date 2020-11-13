# Задание 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_el_idx = 0
max_el_idx = 0

for el in range(len(array)):
    if array[el] > array[max_el_idx]:
        max_el_idx = el
    if array[el] < array[min_el_idx]:
        min_el_idx = el


if min_el_idx > max_el_idx:
    min_el_idx, max_el_idx = max_el_idx, min_el_idx

el_sum = 0
for el in range(min_el_idx+1, max_el_idx):
    el_sum += array[el]

print (f"Сумма элементов, находящихся между наибольшим и наименьшим, равна {el_sum}")