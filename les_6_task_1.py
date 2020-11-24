import random
import timeit
import sys, os
import platform

SIZE = 10
MIN_ITEM = 0
MAX_ITEM =100

def find_func_var1(my_array):   #решение, которое было в предыдущем ДЗ
    if my_array[0] > my_array[1]:
        min_nums = [my_array[0], my_array[1]]
    else:
        min_nums = [my_array[1], my_array[0]]

    for i in range(2, len(my_array)):
        if my_array[i] < min_nums[0]:
            if my_array[i] < min_nums[1]:
                min_nums[0] = min_nums[1]
                min_nums[1] = my_array[i]
            else:
                min_nums[0] = my_array[i]
    memory_items = {}
    sum_memory = 0
    memory_items["min_nums"] = sys.getsizeof(min_nums)
    memory_items["my_array"] = sys.getsizeof(my_array)
    print(f"Потребители памяти: {memory_items}")
    for el in memory_items:
        sum_memory += memory_items[el]
    print(f"Суммарный объем занимаемой памяти: {sum_memory}")

    #print(min_nums.__sizeof__())
    #print(sys.getsizeof(min_nums))
    #print(my_array.__sizeof__())
    #print(sys.getsizeof(my_array))
    return f"Два наименьших числа: {min_nums}"

def find_func_var2(my_array):           #два раза прогоняем алгоритм "пузырька"
    for i in range(len(my_array) - 1):
        if my_array[i]<my_array[i+1]:
            my_array[i], my_array[i+1] = my_array[i+1], my_array[i]

    for i in range(len(my_array) - 2):
        if my_array[i]<my_array[i + 1]:
            my_array[i], my_array[i + 1] = my_array[i + 1], my_array[i]
    #print(my_array)

    memory_items = {}
    sum_memory = 0
    memory_items["my_array"] = sys.getsizeof(my_array)
    print(f"Потребители памяти: {memory_items}")
    for el in memory_items:
        sum_memory += memory_items[el]
    print(f"Суммарный объем занимаемой памяти: {sum_memory}")

    return f"Два наименьших числа: {my_array[len(my_array)-1]}, {my_array[len(my_array)-2]}"

def find_func_var3(my_array, max_el_num):           #Полностью отсортируем массив
    compl_fl = True
    for i in range(max_el_num-1):
        if my_array[i] > my_array[i+1]:
            my_array[i],  my_array[i + 1] = my_array[i + 1],  my_array[i]
            compl_fl = False



    if compl_fl == True:
        #print(f"answ: {my_array}")
        # print(my_array)

        memory_items = {}
        sum_memory = 0
        memory_items["my_array"] = sys.getsizeof(my_array)
        memory_items["compl_fl"] = sys.getsizeof(compl_fl)
        memory_items["max_el_num"] = sys.getsizeof(max_el_num)
        print(f"Потребители памяти: {memory_items}")
        for el in memory_items:
            sum_memory += memory_items[el]
        print(f"Суммарный объем занимаемой памяти: {sum_memory}")
        return (f"Два наименьших числа: {my_array[0]}, {my_array[1]}")
    else:
        #print(my_array)
        return(find_func_var3(my_array, max_el_num - 1))


print(f"Разрядность интерпретатора: {sys.platform}")

print("\n\nИсследование первого варианта функции")
COUNT = 3
list_size = [SIZE * 10 ** i for i in range(COUNT)]

for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    print(f"Длина массива {ar_len}")
    find_func_var1(array)

print("\n\nИсследование второго варианта функции")
COUNT = 5
list_size = [SIZE * 10 ** i for i in range(COUNT)]
for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    find_func_var2(array)


sys.setrecursionlimit(1000000)
print("\n\nИсследование третьего варианта функции")
COUNT = 3
list_size = [SIZE * 10 ** i for i in range(COUNT)]
for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    find_func_var3(array, len(array))
    
    