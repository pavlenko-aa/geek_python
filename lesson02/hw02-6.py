good_1 = input("Введите название первого товара: ")
price_1 = input("Введите цену первого товара: ")
amount_1 = input("Введите количество первого товара: ")
good_2 = input("Введите название второго товара: ")
price_2 = input("Введите цену второго товара: ")
amount_2 = input("Введите количество второго товара: ")
good_3 = input("Введите название третьего товара: ")
price_3 = input("Введите цену третьего товара: ")
amount_3 = input("Введите количество третьего товара: ")
goods = [good_1, good_2, good_3]
prices = [price_1, price_2, price_3]
amounts = [amount_1, amount_2, amount_3]
i=0
for el in goods, prices, amounts:
    nomenc = {f"Название: {goods[i]}, Цена: {prices[i]}, Количество: {amounts[i]}, ед. изм.: шт."}
    print(i+1, nomenc)
    i +=1