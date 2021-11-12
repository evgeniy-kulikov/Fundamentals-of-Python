""" Homework for the Lesson_05 """
""" Task 03 """

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('Task_03_text.txt', 'r', encoding='utf-8') as my_file:
    salary = 0
    count = 0
    low_salary = []
    content = my_file.read().split('\n')
    for i in content:
        i = i.split()
        if int(i[1]) < 20_000:
            low_salary.append(i[0])
        salary += int(i[1])
        count += 1
print('Оклад меньше 20 000:')
for i in low_salary:
    print(i)
print(f'\nсредний оклад сотрудников:\n{round((salary / count), 2)}')
