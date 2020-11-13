# Задание 5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_otr_el = None
for el in array:
    if el < 0 and (max_otr_el == None or el > max_otr_el):
        max_otr_el = el
if(max_otr_el != None):
    print(f"Максимальный отрицательный элемент: {max_otr_el}")
else:
    print("Отрицательных элементов не найдено")
