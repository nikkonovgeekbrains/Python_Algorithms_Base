print("Введите три различных числа: ")
num1 = float(input("num1: "))
num2 = float(input("num2: "))
num3 = float(input("num3: "))

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(f"Среднее по величине число: {num2}")
        else:
            print(f"Среднее по величине число: {num3}")
    else:
        print(f"Среднее по величине число: {num1}")
else:
    if num2 < num3:
        print(f"Среднее по величине число: {num2}")
    else:
        if num1 > num3:
            print(f"Среднее по величине число: {num1}")
        else:
            print(f"Среднее по величине число: {num3}")

