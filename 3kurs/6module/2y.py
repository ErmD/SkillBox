# # ============================== Задача № 1 ==================================
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }

# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }

# big_storage.update(small_storage)
# print(big_storage)

# find_product = big_storage.get(input('Введите наименование: '))
# if find_product == None:
#     print('Товар не найден')
# else:
#     print(find_product)

# # ============================== Задача № 2 ==================================
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# summ = 0.0
# min_cost = None
# min_name = ''

# for name, cost in incomes.items():
#     summ += cost
#     if min_cost is None or min_cost > cost:
#         min_cost = cost
#         min_name = name

# incomes.pop(min_name)
# print('Общий доход за год составил', summ, 'рублей')
# print('Самый маленький доход у', min_name + '. Он составляет', min_cost)
# print('Итоговый словарь:', incomes)

# ============================== Задача № 3 ==================================
text = input('Введите тест: ').lower()

text_dict = {}

for char in text:
    if char in text_dict:
        text_dict[char] += 1
    else:
        text_dict[char] = 1

for i_sym in sorted(text_dict.keys()):
    print(i_sym, ' : ', text_dict[i_sym])
print('Максимальное:', max(text_dict.values()))