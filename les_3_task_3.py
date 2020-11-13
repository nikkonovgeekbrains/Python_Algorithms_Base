# Задание 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

#print(min_el_idx, max_el_idx)

array[min_el_idx], array[max_el_idx] = array[max_el_idx], array[min_el_idx]

print(f"Полученный массив: {array}")