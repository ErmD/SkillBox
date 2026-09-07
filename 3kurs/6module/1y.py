# # =============================== Задание № 1 ========================================
# num = int(input('Введите num = '))
# dict = {}

# for numbers in range(1, num + 1):
#     dict[numbers] = numbers**2

# print(dict)

# # =============================== Задание № 2 ========================================
# info = input('Введите информацию о студенте через пробел:\n(Имя, Фамилия, Город, Место учебы, Оценки)\n')
# info = info.split()
# student_dict = dict()


# if len(info) >= 4:
#     student_dict['Имя'] = info[0]
#     student_dict['Фамилия'] = info[1]
#     student_dict['Город'] = info[2]
#     student_dict['Место учебы'] = info[3]
#     if len(info) > 4:
#         student_dict['Оценки'] = info[4:]
#     else:
#         student_dict['Оценки'] = ''

#     print('\n')
#     for i_info in student_dict:
#         print(i_info, ' - ', student_dict[i_info])
# else:
#     print('Ошибка! Неправильно указаны данные!')

# =============================== Задание № 3 ========================================

contacts = {}

while True:
    print('\n\nТекущий список контактов:')
    if len(contacts) > 0:
        for con in contacts:
            print(con, ' - ', contacts[con])
    else:
        print('<Пусто>')

    info = input('\nВведите информацию для создания контакта (имя номер)\nили "отмена" для выхода:\n')
    info = info.split()
    if 'отмена' in info:
        break
    elif info[0] in contacts:
        print('\n\nТакое Имя уже существует')
    else:
        contacts[info[0]] = info[1]