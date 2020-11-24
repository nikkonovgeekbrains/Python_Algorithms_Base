import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

def bubble_sort(arr):
    n = 1
    while n < len(arr):
        sort_flag = True                #Флаг того, что массив отсортирован
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sort_flag = False       #Если была выполнена хоть одна перестановка, то массив может быть неотсортированным
        if sort_flag == True:
            return arr
        print (arr)
        n += 1
    return arr
a = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]

print(bubble_sort(a))


