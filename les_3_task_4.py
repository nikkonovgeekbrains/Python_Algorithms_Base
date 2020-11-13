# Задание 4
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num_info = {}

for el in array:
    if el in num_info:
        num_info[el] += 1
    else:
        num_info[el] = 1

print(num_info)
max_count = 0
max_count_nums = []
for el in num_info.keys():
    if num_info.get(el) > max_count:
        max_count_nums = []
        max_count_nums.append(el)
        max_count = num_info.get(el)
    elif num_info.get(el) == max_count:
        max_count_nums.append(el)

print(f"Чаще всего встечаются числа: {max_count_nums}({max_count} раз)")


