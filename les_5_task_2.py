from collections import deque
def hex_sum(num1, num2, one_pl):
    if ord(num1.lower()) >= ord("a") and ord(num1.lower()) <= ord("f"):
        num1 = 10 + ord(num1.lower()) - ord("a")
    else:
        num1 = int(num1)

    if ord(num2.lower()) >= ord("a") and ord(num2.lower()) <= ord("f"):
        num2 = 10 + ord(num2.lower()) - ord("a")
    else:
        num2 = int(num2)

    hex_sum = num1 + num2 + int(one_pl)
    if hex_sum < 16:
        one_pl = False
    else:
        hex_sum -= 16
        one_pl = True

    if hex_sum < 10:
        answ_ch = str(hex_sum)
    else:
        answ_ch = chr(ord('a') + hex_sum - 10)

    return answ_ch, one_pl


n1 = list(input("Введите первое число: "))
n2 = list(input("Введите второе число: "))

print(n1)
print(n2)

if len(n2) > len(n1):
    n1, n2 = n2, n1

one_pl_fl = False
answr = deque()
for i in range(len(n1)):
    if i < len(n2):
        new_chr, one_pl_fl = hex_sum(n1[len(n1)-i-1], n2[len(n2)-i-1], one_pl_fl)
    else:
        new_chr, one_pl_fl = hex_sum(n1[len(n1) - i - 1], "0",one_pl_fl)
    answr.appendleft(new_chr)
if one_pl_fl == True:
    answr.appendleft("1")

#print(hex_sum('f','f', True))
print(f"Сумма двух чисел: {''.join(answr).upper()}")



