"""Homework for the Lesson_04"""
from sys import argv

""" Task 01 """
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

try:
    script_name = argv[0]
    work_hours = float(argv[1])
    employee_rate = float(argv[2])
    premium = float(argv[3])
    print('Часовая выработка сотрудника: ', work_hours)
    print('Размер часовой ставки сотрудника: ', employee_rate)
    print('Размер премии сотрудника: ', premium)
    result = work_hours * employee_rate + premium
    print(f'Заработная плата сотрудника составляет:  {result}')
except ValueError:
    print('Необходимо ввести числовое значение!')
