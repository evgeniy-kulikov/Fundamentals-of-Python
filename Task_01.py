"""Homework for the Lesson_02"""

""" Task 01 """
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка указать явно, в программе.

my_list = [7, 5, 3, 'This is', 'my list', True, None]
print(f'Variable "my_list" is of type {type(my_list)}')
for i in range(0, len(my_list)):
    print(f'Element "{my_list[i]}" is of type {type(my_list[i])}')
