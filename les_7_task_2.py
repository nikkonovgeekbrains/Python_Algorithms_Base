import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

#Функция, отвечающая непосредственно за слияние двух списков
def merge_func(lelf_arr, right_arr):
    res_arr = []
    i = 0
    j = 0
    while i < len(lelf_arr) and j < len(right_arr):
        if lelf_arr[i] < right_arr[j]:
            res_arr.append(lelf_arr[i])
            i += 1
        else:
            res_arr.append(right_arr[j])
            j += 1
    while i < len(lelf_arr):
        res_arr.append(lelf_arr[i])
        i += 1
    while j < len(right_arr):
        res_arr.append(right_arr[j])
        j += 1
    return res_arr

def merge_sort(arr):
    #print(arr)
    if len(arr)<2:
        return arr
    else:
        mid = int(len(arr)/2)
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])
        return merge_func(left_arr, right_arr)

a = [MIN_ITEM + (MAX_ITEM - MIN_ITEM) * random.random() for _ in range(SIZE)]
print(a)
print(merge_sort(a))
