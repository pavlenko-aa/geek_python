my_list = [15, 10, 4, 3, 2]
user_numb = int(input("Введите любое натуральное число: "))
i = len(my_list)-1
while i > 0 and user_numb > my_list[i]:
    i -= 1
else:
    my_list.insert(i+1, user_numb) if user_numb < my_list[0] else my_list.insert(0, user_numb)
    print(my_list)
