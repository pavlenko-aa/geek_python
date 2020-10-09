beginning = int(input("Введите начальную дистанцию:"))
desired = int(input("Введите желаемую дистанцию:"))
day = 1
print("Результат: \n1-й день:", beginning, "км")
while beginning < desired:
    beginning = beginning * 1.1
    day += 1
    print(f"{day}-й день: {beginning:.2f} км")
else:
    print(f"Ответ: На {day}-й день спортсмен достигнет результат - не менее {desired} км.")