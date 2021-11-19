""" Homework for the Lesson_05 """
""" Task 04 """

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

# Методы класса: движение поворот, скорость
    def go(self):
        print('Start of movement')

    def stop(self):
        print('Stop of movement')

    def turn(self, direction):  # метод принимает значение
        print(f'Change of direction to the {direction}')

    def show_speed(self):
        print(f'Current speed {self.speed} km/h')


class TownCar(Car):  # дочерний класс с переопределением значения "show_speed"
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Travel speed > 60 km/h. Over speed!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Travel speed > 40 km/h. Over speed!')


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 160:
            print('Be careful!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)  # Переопределяем констркутор для изменения свойства "is_police"

    def is_police(self):
        if self.is_police:
            return f'is from police department'
        else:
            return f'is not from police department'


car_town = TownCar(80, 'Blue', 'Opel')
car_work = WorkCar(50, 'Green', 'Renault')
car_sport = SportCar(180, 'Red', 'Renault')
car_police = PoliceCar(90, 'Special paint', 'Company car')

car_town.show_speed()
car_town.speed = 60  # изменяем скорость
car_town.show_speed()
print(f'Car model "{car_work.name}", color "{car_work.color}"\n')
car_police.turn('left\n')  # изменение направления движения
print(f'Is {car_police.name} a police car?\nanswer: {car_police.is_police}')  # проверка принадлежности к полиции
print(f'Is {car_work.name} a police car?\nanswer: {car_work.is_police}\n')
car_sport.go()
car_sport.show_speed()
