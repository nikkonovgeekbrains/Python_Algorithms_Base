# Задание 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM =100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    min_nums = [array[0], array[1]]
else:
    min_nums = [array[1], array[0]]

for i in range(2,len(array)):
    if array[i] < min_nums[0]:
        if array[i] < min_nums[1]:
            min_nums[0] = min_nums[1]
            min_nums[1] = array[i]
        else:
            min_nums[0] = array[i]

print(f"Два наименьших числа: {min_nums}")

