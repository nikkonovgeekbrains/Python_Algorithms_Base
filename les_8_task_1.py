import hashlib

str1 = "abcda"



"""
Альткрнативный вариант перебора подстрок (просто экспериментировал)
for i in range(len(str1)):
    for j in range(len(str1) - i):
        sub_str = str1[i : i + j+1]
        print( "1::",sub_str)
        if not hashlib.sha256(sub_str.encode('utf-8')).hexdigest() in str_set:
            str_set.add(hashlib.sha256(sub_str.encode('utf-8')).hexdigest())
            print(f"Подстрока {sub_str} уникальна!")
"""

def proc_uniq_sub_str(inp_str):
    str_set = set()
    uniq_count = 0
    for i in range(len(inp_str) - 1):          #Минус один чтобы не включать строку целиком
        j = 0
        while j < len(inp_str) - i:
            sub_str = inp_str[j : j + i + 1]
            #print("1::", sub_str)              #Отлаживал разбиение на подстроки
            j += 1
            if not hashlib.sha256(sub_str.encode('utf-8')).hexdigest() in str_set:
                str_set.add(hashlib.sha256(sub_str.encode('utf-8')).hexdigest())
                uniq_count += 1
                #print(f"Подстрока {sub_str} уникальна!")      #Раскомментировать чтобы посмотреть уникальные подсточки
    #print(f"Количество уникальных подстрок: {uniq_count}")
    return uniq_count


str1 = input("Введите исходную строку: ")
print(f"Строка {str1} содержит {proc_uniq_sub_str(str1)} уникальных подстрок (не считая пустую и строку целиком)")



