"""Homework for the Lesson_03"""

""" Task 02 """
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, year, city, email, telephone):
    return '  '.join([name, surname, year, city, email, telephone])


result = user_data(name='Ivan',
                   surname='Sokolov',
                   year='1989',
                   city='St.Petersburg',
                   email='ivan-sokol@google.com',
                   telephone='+7(802)123-45-67')
print(result)
