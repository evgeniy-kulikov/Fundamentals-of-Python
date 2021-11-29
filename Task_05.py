from datetime import datetime, time

""" Homework for the Lesson_08 """
""" Task 05 """

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class OfficeStorage:  # Склад оргтехники. Общее описание
    num1 = 0
    num2 = 0

    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        # внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number: [equipment.title, str(t.date())]})
        OfficeStorage.num1 += 1
        return f'На склад {self.title} получено оборудование: {equipment.title}, ' \
               f'серийный номер: {str(equipment.serial_number)}, ' \
               f'Дата приема: {str(t.day)}.{str(t.month)}.{str(t.year)}'

    def give_to_depot(self, equipment):
        # передача оборудование на другой склад или подразделение
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title, t.date()]})
        OfficeStorage.num2 += 1
        return f'На склад {self.title} передано оборудование: {equipment.title} ,' \
               f'серийный номер: {str(equipment.serial_number)}, ' \
               f'Дата передачи: {str(t.day)}.{str(t.month)}.{str(t.year)}'


class OfficeEquipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return f'Оборудование: {str(self.title)}, s/n: {self.serial_number}'


class Printer(OfficeEquipment):
    def __init__(self, title, serial_number, print_type):
        OfficeEquipment.__init__(self, title, serial_number)
        self.print_type = print_type

    def printer_info(self):
        return f'Название модели: {self.title}, тип: {self.print_type}, s/n: {self.serial_number}'


class Scanner(OfficeEquipment):
    def __init__(self, title, serial_number, resolution):
        OfficeEquipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def scanner_info(self):
        return f'Название модели: {self.title}, разрешение: {str(self.resolution)} dpi, s/n: {self.serial_number}'


class Copier(OfficeEquipment):
    def __init__(self, title, serial_number, type_of_feed):
        OfficeEquipment.__init__(self, title, serial_number)
        self.type_of_feed = type_of_feed

    def copier_info(self):
        return f'Название модели: {self.title}, тип сканера: {self.type_of_feed}, s/n: {self.serial_number}'


store1 = OfficeStorage('Основной')
printer1 = Printer('Kyocera P3145DN', 62416345, 'лазерный')
scanner1 = Scanner('EPSON Perfection V850', 654321, 2400)
print(store1.take_to_depot(printer1))
store1.take_to_depot(scanner1)
print(f'Общий список оборудования: {store1.lists}')
print(f'Кол-во техники на складе "{store1.title}": {store1.num1} шт.')

copier1 = Copier('Xerox WorkCentre 6400S', 77143234, 'планшетный/протяжный')
store2 = OfficeStorage('Филиал')
print(f'\n{store2.give_to_depot(copier1)}')
print(store2.give_lists)
print(f'Кол-во техники на складе "{store2.title}": {store2.num2} шт.')
