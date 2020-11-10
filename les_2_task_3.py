def num_reverse(num):
    res = 0
    while num > 0:
        res = res*10 + num%10
        num = int(num/10)
    return res

n = int(input("Введите число: "))
print(f"Перевернутое число: {num_reverse(n)}")