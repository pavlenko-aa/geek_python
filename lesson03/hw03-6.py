def int_func(a):
    if a.islower():
        return a.title()
    else:
        return f"Слово {a} начинается не с маленькой буквы"


user_line = list(map(str, input("Введите строку из латинских слов с маленькой буквы, разделённых пробелом: ").split()))

line_changed = list()
for el in user_line:
    el_new = int_func(el)
    line_changed.append(el_new)

print("Ваша строка: ", ' '.join(line_changed))
