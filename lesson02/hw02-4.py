sentence = input("Введите несколько слов, разделяя их пробелом: ")
sentence_new = sentence.split()
for ind, el in enumerate(sentence_new, 1):
    print(ind, el[:10])