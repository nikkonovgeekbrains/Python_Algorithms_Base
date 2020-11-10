num1 = int(input("Введите натуральное число: "))
even_count = 0
odd_count = 0

while num1 > 0:
    if num1%2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num1 = int(num1/10)

print(f"Количество четных чисел: {even_count} \nКоличество нечетных чисел: {odd_count}")
