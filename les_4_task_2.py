import timeit

def with_Erast_func(num,max_num = 1000):
    temp_array = [i for i in range (max_num+1)]
    #print(temp_array)

    m = 2
    while m < max_num:
        if temp_array[m] != 0:
            j = m * 2
            while j < max_num:
                temp_array[j] = 0
                j = j + m
        m += 1
    answ_array = []
    for i in temp_array:
        if temp_array[i] != 0:
            answ_array.append(temp_array[i])

    del temp_array
    return answ_array[num]

def without_Erast_func(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        cur_num = 2
        cur_easy_num = 2
        while(cur_easy_num < num):
            cur_num += 1
            easy_fl = True
            for i in range(2,cur_num-1):
                if cur_num % i == 0:
                    easy_fl = False
                    break
            #print(cur_easy_num)
            if easy_fl == True:
                cur_easy_num += 1
        return cur_num


print(with_Erast_func(10))
print(without_Erast_func(10))

print(f"Время выполнения с ситом {timeit.timeit('with_Erast_func(10)', number = 100, globals = globals())}")
print(f"Время выполнения без сита ситом {timeit.timeit('without_Erast_func(10)', number = 100, globals = globals())}")
