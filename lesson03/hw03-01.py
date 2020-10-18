def div(divid, divis):
    try:
        return divid / divis
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
a = 0
while not a:
    try:
        divid = int(input("Введите делимое: "))
        a = 1
    except ValueError:
        print("Введите цифровое значение!")

a = 0
while not a:
    try:
        divis = int(input("Введите делитель: "))
        a = 1
    except ValueError:
        print("Введите цифровое значение!")


print("Результат: ", div(divid, divis))