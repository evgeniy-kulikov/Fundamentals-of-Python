""" Homework for the Lesson_05 """
""" Task 01 """

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('Task_01_text.txt', 'w') as my_file:
    line = input('Введите текст: ')
    while line:
        my_file.writelines(line + '\n')
        line = input(f'Введите текст: ')
        if not line:
            break

with open('Task_01_text.txt', 'r') as my_file:
    content = my_file.read()
    print(f'\nСодержимое файла:\n{content}')
