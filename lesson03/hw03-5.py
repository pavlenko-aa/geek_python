summa = 0


def sequence_new(x):
    global summa
    for el in x:
        if el == "#":
            return False
        el = int(el)
        summa = summa + el
    return True


sequence = input("Введите строку чисел, разделяя их пробелом: ").split()

res = sequence_new(sequence)
print("Сумма чисел:", summa)

while res:
    sequence_2 = input("Вы можете ввести новую строку чисел, разделяя их пробелом.\n"
                    "Введённые числа после нажатия кнопки Enter добавятся к полученной ранее сумме.\n"
                    "Если вы хотите прекратить добавление чисел, введите #: ").split()
    res = sequence_new(sequence_2)
    print("Сумма чисел:", summa)
