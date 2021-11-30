""" Homework for the Lesson_08 """
""" Task 04 """

# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class OfficeStorage:  # Склад оргтехники. Общее описание
    def __init__(self, title):
        self.title = title


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


store1 = OfficeStorage('Основной склад')
store2 = OfficeStorage('Филиал')
print(store1.title)
print(store2.title)

equipment1 = OfficeEquipment('Сканер', 123456)
print(equipment1.__str__())

printer1 = Printer('Kyocera P3145DN', 62416345, 'лазерный')
print(printer1.printer_info())

scanner1 = Scanner('EPSON Perfection V850', 654321, 2400)
print(scanner1.scanner_info())

copier1 = Copier('Xerox WorkCentre 6400S', 77143234, 'планшетный/протяжный')
print(copier1.copier_info())
