# Задание 1
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9
MIN_FIG = 2
MAX_FIG = 9

MAX_NUM = 99

answ_array = []
for i in range(MIN_FIG, MAX_FIG+1):
    el_count = 0
    for el in range (i,MAX_NUM+1):
        if el%i == 0:
            el_count += 1
    answ_array.append(el_count)

for el in range(MIN_FIG, MAX_FIG+1):
    print(f"Числу {el} кратно {answ_array[el-MIN_FIG]} в диапазоне от {MIN_FIG} до {MAX_NUM}")