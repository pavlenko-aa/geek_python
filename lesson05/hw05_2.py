"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. """

my_f = open("my_file2.txt", "r")
i = 0
for line in my_f:
    i +=1
    b = len(line.split())
    print(f"Количество слов в строке {i} составляет {b}")
print(f"Количество строк в файле: {i}")
my_f.close()