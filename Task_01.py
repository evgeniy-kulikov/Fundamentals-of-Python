"""Homework for the Lesson_04"""
from sys import argv

""" Task 01 """
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

script_name, work_hours, employee_rate, premium = argv

work_hours = float(work_hours)
employee_rate = float(employee_rate)
premium = int(premium)

print('Часовая выработка сотрудника: ', work_hours)
print('Размер часовой ставки сотрудника: ', employee_rate)
print('Размер премии сотрудника: ', premium)


def salary_employee():
    result = work_hours * employee_rate + premium
    print(f'Заработная плата сотрудника составляет:  {result}')


salary_employee()
