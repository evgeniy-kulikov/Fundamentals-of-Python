""" Homework for the Lesson_08 """
""" Task 04 """

# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class OfficeStorage:  # Склад оргтехники. Общее описание
    def __init__(self):
        pass


class OfficeEquipment:  # Оргтехника. Родительский класс для дочерних данного оборудования
    def __init__(self, name, series, amount, price):
        self.name = name
        self.series = series
        self.amount = amount
        self.price = price
        self.group = {'Производитель': self.name, 'Модель': self.series, 'Количество': self.amount, 'Цена': self.price}

    def group_name(self):  # Вид оборудования (в данной реализации - дочерние классы (OfficeEquipment))
        return f'Вид оборудования: {self.group}'


ee = OfficeStorage()
ee.name = 'jvjkv'
print(ee.name)








