# #  =============================== Задача № 1 =======================================

# menu = [word.title() for word in 'утиное филе;фланк-стейк;банановый пирог;плов'.split(';')]
# print('Меню:', ', '.join(menu))

# #  =============================== Задача № 2 =======================================

# line = input('Введите строку: ')

# res = []
# for char in line:
#     if res and res[-1][-1] == char:
#         res[-1] += char
#     else:
#         res.append(char)
        
# res = ''.join([el[0] + str(len(el)) for el in res])

# print(res)

# #  =============================== Задача № 3 =======================================

# line = input('Первая строка: ')
# shifted_line = input('Вторая строка: ')

# len_line = len(line)

# if len_line == len(shifted_line):
#     if line[0] in shifted_line:
#         shift = shifted_line.index(line[0])
#         for index, char_line in enumerate(line):
#                 if char_line != shifted_line[(index+shift)%len_line]:
#                     print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
#                     break
#                 else:
#                     print('Первая строка получается из второй со сдвигом', shift)
#     else:
#         print('Ошибка, разные символы в строках!')
    
# else:
#     print('Ошибка, разные по длине строки!')

# ============================= Задача № 4 =====================================

data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.docx  important_info.docx notes1900.docx"]],
    ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]

new_data = []
extensions = ('.txt', '.docx') # Расширения файлов
symbols = '@№$%^&*()' # Запретные символы в начале имени файла

for el in data: # Перебираем все элементы в data
    ip = el[0].split('.') # Достаем ip адрес
    if len(ip) == 4:
        for number in ip:
            if number.isdigit(): #
                if int(number) > 255 or int(number) < 0:
                    break
            else:
                break
        else:
            files = el[1][0].split(' ') # Создаем массив со всеми файлами
            index_files_remove = [] # Список индексов для удаления
            for index, file in enumerate(files):
                if len(file) == 0 or file[0] in symbols or file.endswith(extensions) == False:
                    index_files_remove.append(index) # Добавляем индекс файла на удаление
            
            for index_file in index_files_remove[::-1]: # Перебираем индексы с начиная с конца для удаления
                files.pop(index_file) # Удаляем неправильный файл по индексу
            el[1] = files # Изменяем список с файлами в элементе
            new_data.append(el) # Добавляем в список
            print(el) # Выводим на экран элемент