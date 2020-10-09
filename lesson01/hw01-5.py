income = int(input("Введите выручку:"))
cost = int(input("Введите издержки:"))
profit = income - cost
if income > cost:
    print("Фирма работает с прибылью!")
    rent = profit / income
    print("Рентабельность: ", rent)
    staff = int(input("Введите численность сотрудников:"))
    prof_staff = float(profit / staff)
    print(f"Прибыль в расчете на сотрудника составляет: {prof_staff:.2f}")
elif income == cost:
    print("Результат деятельности нулевой.")
else:
    print("Фирма работает с убытком!")
