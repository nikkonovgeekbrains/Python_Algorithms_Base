import random

M_SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20

a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * M_SIZE + 1)]

print(f"Исходный массив: {a}")

#Функция быстрой сортирки из книги Горкаем алгоритмы
#ВАЖНО: использую ее только как эталон для проверки!
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def find_mid_func(arr):
    print("\n \n Работа функции:")
    if len(arr) < 2:
        return arr[0]          #Медиана массива из одного элемента и есть этот элемент
    else:
        temp_arr = arr
        arr_shift = 0
        mid_el = None
        mid_ind = int(len(arr) / 2)
        while len(arr) > 0:
            pivot = arr[0]
            less_arr = [i for i in arr[1:] if i <= pivot]
            greater_arr = [i for i in arr[1:] if i > pivot]
            print(f"Результат разбиения: {less_arr}    {pivot}    {greater_arr}")
            if len(less_arr) + arr_shift == mid_ind:    #Если базовый элемент попадает на место медианного (с учетом сдвига)
                mid_el = pivot
                break
            elif len(less_arr) + arr_shift > mid_ind:   #Если медианный элемент находится где-то в списке наимеменьших относительно базового элементов
                arr = less_arr
            else:                                       #Если медианный элемент находится где-то в списке наибольших относительно базового элементов
                arr_shift += len(less_arr) + 1
                arr = greater_arr
            print(arr)
            print(arr_shift)
            print(f"Работаем с подмассивом {arr} с общим сдвигом {arr_shift}")
        return mid_el

etalon_mid = quicksort(a)[int(len(a) / 2)]
print(f"Отсортированный массив: {quicksort(a)} c медианой {etalon_mid}")

my_find_mid = find_mid_func(a)
print(f"Медианоя является (результат выполнения своей функции): {my_find_mid}")

if my_find_mid == etalon_mid:
    print("\nНайденный результат совпал с эталонным.")
else:
    print("Найденный результат не совпадает с эталонным. Что-то пошло не так!")



