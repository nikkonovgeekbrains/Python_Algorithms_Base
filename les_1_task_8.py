year = int(input("Введите номер года: "))
if year > -9:
    if year >= 8:
        if year % 4 == 0:
            if year > 1582:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("Это не високосный год")
                    else:
                        print("Это не високосный год")
                else:
                    print("Это високосный год")
            else:
                print("Это високосный год")
        else:
            print("Это не високосный год")
    else:
        print("Это не високосный год")
else:
    if year >= -42:
        if year % 3 == 0:
            print("Это високосный год")
        else:
            print("Это не високосный год")
    else:
        print("Это не високосный год")
