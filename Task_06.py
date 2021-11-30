from datetime import datetime

""" Homework for the Lesson_08 """
""" Task 06 """

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class OfficeStorage:  # Склад оргтехники. Общее описание
    num1 = 0
    num2 = 0

    def __init__(self, title):
        self.title = title
        self.lists = {}  # Полученное оборудование
        self.give_lists = {}  # Переданное оборудование

    def take_to_depot(self, equipment):
        # внесение в словарь название оборудования, количество и время передачи на склад
        t = datetime.now()
        self.lists.update({t.ctime(): [equipment.title, equipment.quantity]})
        OfficeStorage.num1 += 1
        return f'На склад {self.title} получено оборудование: {equipment.title}, ' \
               f'количество: {str(equipment.quantity)} шт., ' \
               f'Дата приема: {str(t.day)}.{str(t.month)}.{str(t.year)}'

    def give_to_depot(self, equipment):
        # внесение в словарь название оборудования, количество и время передачи на склад подразделения
        t = datetime.now()
        self.give_lists.update({t.ctime(): [equipment.title, equipment.quantity]})
        OfficeStorage.num2 += 1
        return f'На склад {self.title} передано оборудование: {equipment.title} ,' \
               f'количество: {str(equipment.quantity)} шт., ' \
               f'Дата передачи: {str(t.day)}.{str(t.month)}.{str(t.year)}'


class OfficeEquipment:
    def __init__(self, title,  quantity):
        self.title = title
        self.quantity = quantity

    # def reception(self):
    #     try:
    #         self.quantity = int(input(f'Введите количество '))
    #     except ValueError:
    #         return f'Ошибка ввода данных'

    def __str__(self):
        return f'Оборудование: {str(self.title)}, кол-во: {self.quantity} шт.'


class Printer(OfficeEquipment):
    def __init__(self, title, print_type, quantity):
        OfficeEquipment.__init__(self, title, quantity)
        self.print_type = print_type

    def printer_info(self):
        return f'Название модели: {self.title}, тип: {self.print_type}, кол-во: {self.quantity()} шт.'


class Scanner(OfficeEquipment):
    def __init__(self, title, resolution, quantity):
        OfficeEquipment.__init__(self, title, quantity)
        self.resolution = resolution

    def scanner_info(self):
        return f'Название модели: {self.title}, разрешение: {str(self.resolution)} dpi, кол-во: {self.quantity} шт.'


class Copier(OfficeEquipment):
    def __init__(self, title, type_of_feed, quantity):
        OfficeEquipment.__init__(self, title, quantity)
        self.type_of_feed = type_of_feed

    def copier_info(self):
        return f'Название модели: {self.title}, тип сканера: {self.type_of_feed}, кол-во: {self.quantity} шт.'


store1 = OfficeStorage('Основной')
num = None
try:
    num1 = int(input('Укажите количество принтеров: '))
except ValueError:
    print('Ошибка ввода данных')
else:
    num = num1
printer1 = Printer('Kyocera P3145DN', 'лазерный', num)
print(store1.take_to_depot(printer1))
print(f'Общий список оборудования: {store1.lists}')
print(f'Кол-во техники на складе "{store1.title}": {store1.num1} шт.')
