from functools import reduce

"""Homework for the Lesson_04"""
""" Task 05 """
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


def multiply_func(num1, num2):
    return num1 * num2


even_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список четных значений:\n{even_list}')
print(f'Результат перемножения всех элементов списка:\n{reduce(multiply_func, even_list)}')
