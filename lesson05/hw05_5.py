"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран. """

timetable_source = open("my_file5.txt", "r")
disciplines = []
hours_spent = []
for line in timetable_source:
    split = line.split(":")
    key = split[0]
    disciplines.append(key)
    new_line = split[1]
    new_line = new_line.replace("-", "")
    new_line = new_line.replace("(л)", "")
    new_line = new_line.replace("(пр)", "")
    new_line = new_line.replace("(лаб)", "")
    summary = 0
    for el in new_line.split():
        el = int(el)
        summary = summary + el
    hours_spent.append(summary)

timetable = {}
i = 0
while i < len(hours_spent):
    timetable[disciplines[i]]=hours_spent[i]
    # timetable.update({diciplines[i]:hours_spent[i]}) Второй вариант
    i += 1

print(timetable)

timetable_source.close()
