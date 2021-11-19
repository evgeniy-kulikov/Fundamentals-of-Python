""" Homework for the Lesson_05 """
""" Task 03 """

# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:  # базовый класс

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):  # класс Position на базе класса Worker

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


user_01 = Position('Александр', 'Овечкин', 'Хоккеист', 1_000_000, 500_000)  # объект класса Position

print(user_01.name)  # вывод атририбута объекта класса Position
print(user_01.surname)
print(user_01.position)
print(f'Фамилия: {user_01.get_full_name()}')  # вывод метода объекта класса Position
print(f'Должность: {user_01.position}')
print(f'Доход: {user_01.get_total_income()}')
