# Задание 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import timeit
import sys
import cProfile

SIZE = 10
MIN_ITEM = 0
MAX_ITEM =100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(array)

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

    return f"Два наименьших числа: {min_nums}"

def find_func_var2(my_array):           #два раза прогоняем алгоритм "пузырька"
    for i in range(len(my_array) - 1):
        if my_array[i]<my_array[i+1]:
            my_array[i], my_array[i+1] = my_array[i+1], my_array[i]

    for i in range(len(my_array) - 2):
        if my_array[i]<my_array[i + 1]:
            my_array[i], my_array[i + 1] = my_array[i + 1], my_array[i]
    #print(my_array)
    return f"Два наименьших числа: {my_array[len(my_array)-1]}, {my_array[len(my_array)-2]}"

def find_func_var3(my_array, max_el_num):           #Полностью отсортируем массив
    compl_fl = True
    for i in range(max_el_num-1):
        if my_array[i] > my_array[i+1]:
            my_array[i],  my_array[i + 1] = my_array[i + 1],  my_array[i]
            compl_fl = False
    if compl_fl == True:
        #print(f"answ: {my_array}")
        return (f"Два наименьших числа: {my_array[0]}, {my_array[1]}")
    else:
        #print(my_array)
        return(find_func_var3(my_array, max_el_num - 1))


print("Исследование первого варианта функции")
COUNT = 5
list_size = [SIZE * 10 ** i for i in range(COUNT)]
for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    print(f"Время выполнения (длина массива {ar_len}): {timeit.timeit('find_func_var1(array)', number = 100, globals = globals())}")
    print (f"cProfile для длина массива {ar_len}:")
    cProfile.run('find_func_var1(array)')

#Время выполнения (длина массива 10): 0.0005745999999999946
#Время выполнения (длина массива 100): 0.0024403000000000064
#Время выполнения (длина массива 1000): 0.014823099999999999
#Время выполнения (длина массива 10000): 0.1398664
#Время выполнения (длина массива 100000): 1.4485459
#Время выполнения (длина массива 1000000): 14.7769912
#Похоже на линейную сложность O(n)

#cProfile для длина массива 10000:
#         8 function calls in 0.010 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#        1    0.010    0.010    0.010    0.010 les_4_task_1.py:32(find_func_var2)
#        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print("Исследование второго варианта функции")
COUNT = 5
list_size = [SIZE * 10 ** i for i in range(COUNT)]
for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    print(f"Время выполнения (длина массива {ar_len}): {timeit.timeit('find_func_var2(array)', number = 100, globals = globals())}")
    print(f"cProfile для длина массива {ar_len}:")
    cProfile.run('find_func_var2(array)')

#Время выполнения (длина массива 10): 0.000525500000001955
#Время выполнения (длина массива 100): 0.004137699999997579
#Время выполнения (длина массива 1000): 0.0770590999999996
#Время выполнения (длина массива 10000): 0.9333173000000023
#Время выполнения (длина массива 100000): 10.5567527
#Время выполнения (длина массива 1000000): 109.13423689999999
#Похоже на линейную сложность O(n)

#cProfile для длина массива 10000:
#         8 function calls in 0.010 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#        1    0.010    0.010    0.010    0.010 les_4_task_1.py:32(find_func_var2)
#        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



sys.setrecursionlimit(1000000)
print("Исследование третьего варианта функции")
COUNT = 3
list_size = [SIZE * 10 ** i for i in range(COUNT)]
for ar_len in list_size:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ar_len)]
    print(f"Время выполнения (длина массива {ar_len}): {timeit.timeit('find_func_var3(array, len(array))', number = 100, globals = globals())}")
    print(f"cProfile для длина массива {ar_len}:")
    cProfile.run('find_func_var3(array, len(array))')

#Время выполнения (длина массива 10): 0.0003688999999997833
#Время выполнения (длина массива 100): 0.003241900000000797
#Время выполнения (длина массива 1000): 0.17931130000000017
#В целом похоже на O(n**2), что соответствует пузырьку
#Делал до 1000 элементов, так как потом при использовании рекурсии кончается память =)

#print(find_func_var2(array))
#print(find_func_var3(array, len(array)))
