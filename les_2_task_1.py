while True:
    oper_type = input("Введите тип операции (+, -, *, /, 0 для выхода):")
    if oper_type == "0":
        break
    else:
        print("Введите два числа")
        a = float(input("n1 = "))
        b = float(input("n2 = "))

        if oper_type == "+":
            print(f"Результат сложения: {a+b}")
        elif oper_type == "-":
            print(f"Результат вычитания: {a-b}")
        elif oper_type == "*":
            print(f"Результат умножения: {a*b}")
        elif oper_type == "/":
            if b == 0:
                print("Деление на 0! Введите другие данные.")
            else:
                print(f"Результат умножения: {a/b}")
        else:
            print("Введен неверный знак!")
print("Выход из цикла")
