# # ================================ Задание № 1 ========================================

# words = input('Введити поисковые слова через запятую: ').split(', ')
# line = input('Введите предложение: ')
# word_count = [line.count(word) for word in words]
# print(word_count)

# # ================================ Задание № 2 ========================================

# text = input('Введите текст: ').split()
# print(' '.join(text))

# ================================ Задание № 3 ========================================

while True:
    template = input('Введите шаблон поздравления используя конструкции {name} и {age}: ')
    if '{name}' in template and '{age}' in template:
        break
    print('Ошибка отсутствуют одна или две конструкции')

name_list = input('Напишите список имен через запятую: ').split(', ')
ages_list = input('Укажите возрасты через пробел: ').split()

for name, age in zip(name_list, ages_list):
    print(template.format(name = name, age = age))

people = [' -> '.join([name_list[index], ages_list[index]]) for index in range(len(name_list))]
print('Именинники:\n' + '\n'.join(people))