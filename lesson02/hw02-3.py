month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
seasons = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

for el in seasons.keys():
    if month in seasons.get(el):
        print("Ваш месяц относится к времени года", el)


    

