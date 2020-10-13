sorting = list(input("Введите любой набор элементов:"))
print("Ваша строка:", sorting)
i = 0
for el in range(int(len(sorting) / 2)):
    sorting[i], sorting[i + 1] = sorting[i + 1], sorting[i]
    i += 2
print("Новая строка: ", sorting)
