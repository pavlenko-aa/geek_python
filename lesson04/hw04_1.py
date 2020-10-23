def calculate(hours, wage, bonus):
    try:
        salary = int(hours * wage + bonus)
        return salary

    except TypeError:
        return


def worker(name):
    print(f"Заработная плата сотрудника {name} составляет: ")

