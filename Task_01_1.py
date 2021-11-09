"""Homework for the Lesson_04"""
from sys import argv

""" Task 01 """
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

""" Вариант с пользовательским вводом данных"""

script_name = argv


def salary_employee():
    try:
        work_hours = float(input('Часовая выработка сотрудника: '))
        employee_rate = float(input('Размер часовой ставки сотрудника: '))
        premium = float(input('Размер премии сотрудника: '))
        result = work_hours * employee_rate + premium
        print(f'Заработная плата сотрудника составляет:  {result}')
    except ValueError:
        return print('Необходимо ввести числовое значение!')


salary_employee()
