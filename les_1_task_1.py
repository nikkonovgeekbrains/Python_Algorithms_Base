n = int(input("Введите трехзначное число: "))
if (n > 99) and (n < 1000):
    n1 = int(n/100)
    n2 = int((n % 100) / 10)
    n3 = n % 10
    my_sum = n1 + n2 + n3
    mult = n1 * n2 * n3
    print(f'Сумма чисел равна {my_sum}')
    print(f'Произведение чисел равно {mult}')
else:
    print("Введенное число не является трехзначным")