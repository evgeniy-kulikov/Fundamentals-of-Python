"""Homework for the Lesson_04"""
from random import randint
""" Task 02 """
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

first_list = [randint(1, 300) for i in range(12)]
print(f'Исходный список:\n{first_list}')

edition_list = [el for i, el in enumerate(first_list) if first_list[i - 1] < first_list[i] and i > 0]
print(f'Измененный список:\n{edition_list}')
