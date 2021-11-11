""" Homework for the Lesson_05 """
""" Task 02 """

# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('less_02_text.txt', 'r') as my_file:
    content = my_file.read()
    print(f'Содержимое файла:\n{content}\n')
with open('less_02_text.txt', 'r') as my_file:
    content = my_file.readlines()
    print(f'Количество строк в файле: {len(content)}')
with open('less_02_text.txt', 'r') as my_file:
    content = my_file.readlines()
    for i in range(len(content)):
        print(f'В строке #{i + 1} кол-во символов: {len(content[i])}')
with open('less_02_text.txt', 'r') as my_file:
    content = my_file.read()
    content = content.split()
    print(f'Общее кол-во слов: {len(content)}')
