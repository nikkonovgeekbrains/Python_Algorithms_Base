def proc_sum(n, cur_sum = 0, cur_el = 1):
    cur_sum += cur_el
    n -= 1
    if n > 0:
        return proc_sum(n,cur_sum, -float(cur_el/2))
    else:
        return cur_sum

num = int(input("Введите количество элементов последовательности: "))
my_sum = proc_sum(num)
print(f"Сумма последовательности равна {my_sum}")