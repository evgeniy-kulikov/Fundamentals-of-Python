""" Homework for the Lesson_05 """
""" Task 04 """

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('Task_04_1_text.txt', 'r', encoding='utf-8') as my_file:
    for i in my_file:
        i = i.split(' ', maxsplit=1)
        new_file.append(dict_rus[i[0]] + ' ' + i[1])
    print(''.join(new_file))

with open('Task_04_2_text.txt', 'w', encoding='utf-8') as my_file:
    my_file.writelines(new_file)
