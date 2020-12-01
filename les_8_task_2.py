inp_str = "beep boop beer!"

char_dict = {}
for i in range(len(inp_str)):
    if char_dict.get(inp_str[i], False):
        char_dict[inp_str[i]] += 1
    else:
        char_dict[inp_str[i]] = 1

print(char_dict)

char_list = list(char_dict.items())
char_list.sort(key=lambda i: i[1])

while len(char_list)>2:
    print("\n\nИсходный:")
    print(char_list)
    if char_list[0][1] + char_list[1][1] >= char_list[2][1]:
        temp_el = ([char_list[0], char_list[1]], char_list[0][1] + char_list[1][1])
        char_list.pop(0)
        char_list[0] = temp_el
        char_list.sort(key=lambda i: i[1])
        print("Получили:")
        print(char_list)

temp_el = ([char_list[0], char_list[1]], char_list[0][1] + char_list[1][1])
char_list.pop(0)
print(char_list)
char_list[0] = temp_el
print("Получили:")
print(char_list)


