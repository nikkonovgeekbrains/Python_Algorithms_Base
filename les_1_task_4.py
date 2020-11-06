import random

print("Введите диапазон для генерации случайного целого числа: ")
i_min = int(input("Наименьшее число равно: "))
i_max = int(input("Наибольшее число равно: "))

print("Введите диапазон для генерации случайного вещественного числа: ")
f_min = float(input("Наименьшее число равно: "))
f_max = float(input("Наибольшее число равно: "))

print("Введите диапазон для генерации случайного символа (a-z): ")
s_min = input("Нижняя граница символов: ")
s_max = input("Верхняя граница символов: ")

int_num = random.randint(i_min, i_max)
f_num = random.uniform(f_min, f_max)
s = chr(random.randint(ord(s_min), ord(s_max)))

print("Случайное вещественное число: {0}, "
      "\nСлучайное вещественное число: {1:.2f}, "
      "\nСлучайный символ: {2}".format(int_num, f_num, s))


