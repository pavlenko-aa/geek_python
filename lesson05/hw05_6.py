""" Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл."""


import json

with open("my_file6.txt") as ventures:
    profit_total = []
    ventures_data = {}
    for line in ventures:
        split = line.split()
        profit = int(split[2]) - int(split[3])
        if profit > 0:
            profit_total.append(profit)
        ventures_data[f"{split[0]} {split[1]}"] = profit
    profit_average = {"average_profit": sum(profit_total) / len(profit_total)}

    with open("json6.json", "w") as write_f:
        json.dump([ventures_data, profit_average], write_f)