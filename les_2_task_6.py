import random

answ_num = random.randint(0,100)

print("Угадайте число от 0 до 100")

for i in range(0,10):
    num = int(input("Введите число от 0 до 100"))
    if num > answ_num:
        print("Загаданное число меньше")
    elif num < answ_num:
        print("Загаданное число больше")
    else:
        print("Вы угадали Число")
        break
else:
    print(f"Вы не угадали. Было загадано число {answ_num}")
