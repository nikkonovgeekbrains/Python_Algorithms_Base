from collections import deque
from collections import namedtuple
firm_list = deque()
print (firm_list)
Firm_info = namedtuple('Firm_info', 'name, incs, sum_inc')
while(True):
    firm_name = input("Введите название фирмы (0 для окончания ввода):")
    if firm_name == "0":
        break
    firm_inc = []
    inc_sum = 0
    for i in range(4):
        firm_inc.append(float(input(f"Введите прибыль фирмы за квартал {i+1}:")))
        inc_sum += firm_inc[i]
    firm_list.append(Firm_info(firm_name, firm_inc, inc_sum))
print(firm_list)

mean_inc = 0
for el in firm_list:
    mean_inc += el.sum_inc
mean_inc = mean_inc / len(firm_list)
print(f"Средний уровень прибыли: {mean_inc}")

up_firm_list = []
down_firm_list = []
if len(firm_list) > 0:
    while len(firm_list) > 0:
        if firm_list[0].sum_inc > mean_inc:
            up_firm_list.append(firm_list.popleft().name)
        elif firm_list[0].sum_inc < mean_inc:
            down_firm_list.append(firm_list.popleft().name)
        else:
            firm_list.popleft()

    print(f"Имена фирм со средней прибылью выше средней: {up_firm_list}")
    print(f"Имена фирм со средней прибылью ниже средней: {down_firm_list}")
else:
    print("Нет данных ни по одной фирме!")



