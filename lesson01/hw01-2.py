time = int(input("Введите время в секундах:"))
time_hour = int(time / 3600)
time_min = int(time % 3600 / 60)
time_sec = int(time % 60)
print(f"Время {time_hour}:{time_min}:{time_sec}")