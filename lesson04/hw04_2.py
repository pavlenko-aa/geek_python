given_list = [300, 301, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [given_list[el] for el in range(1, len(given_list) - 1) if given_list[el] > given_list[el-1]]

print(new_list)