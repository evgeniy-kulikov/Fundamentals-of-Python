"""Homework for the Lesson_03"""

""" Task 03 """
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    func_list = sorted([arg1, arg2, arg3])
    return func_list[1] + func_list[2]


num_1 = int(input('Введите 1-е целое число: '))
num_2 = int(input('Введите 2-е целое число: '))
num_3 = int(input('Введите 3-е целое число: '))

result = my_func(num_1, num_2, num_3)
print(f'Сумма наибольших 2-х чисел: {result}')
