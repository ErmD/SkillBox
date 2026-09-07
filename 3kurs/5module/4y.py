# #  ===================================== Задача № 1 =========================================

# line = input('Введите сообщение: ')
# shift = int(input('Введите сдвиг: '))

# russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# encrypted_line = ''.join([(russian_alphabet[(russian_alphabet.index(letter.lower()) + shift) % len(russian_alphabet)] if letter.lower() in russian_alphabet else letter.lower()) for letter in line])
# print(encrypted_line)

# #  ===================================== Задача № 2 =========================================

# path = input('Путь к файлу: ')
# cd = input('На каком диске должен лежать файл: ')
# file_format = input('Требуемое расширение файла: ')

# if not path.startswith(cd):
#     print('Ошибка, неправильный диск!')
# elif not path.endswith(file_format):
#     print('Ошибка, неправильное расширение файла!')
# else:
#     print('Путь корректен!')

#  ===================================== Задача № 3 =========================================

line = input('Введите строку: ')
lowers = len([letter for letter in line if letter.islower()])
uppers = len([letter for letter in line if letter.isupper()])

if lowers > uppers:
    print(line.lower())
else:
    print(line.upper())