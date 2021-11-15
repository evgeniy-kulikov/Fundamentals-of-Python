""" Homework for the Lesson_05 """
""" Task 05 """

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

""" Записываем числа в файл """
try:
    with open('Task_05_text.txt', 'w', encoding='utf-8') as my_file:
        user_line = input('Введите цифры через пробел: ')
        my_file.writelines(user_line)
        user_num = user_line.split()
        print(f'Сумма введенных чисел равна: {sum(map(int, user_num))}')
except IOError:
    print('Произошла ошибка ввода-вывода!')
except ValueError:
    print('Необходимо вводить только целые числа')


""" Суммируем записанные числа из файла """
sum_num = 0
with open('Task_05_text.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readline()
    for i in content.split():
        sum_num += int(i)
    print(f'Сумма записанных чисел в файле "Task_05_text.txt" равна: {sum_num}')
