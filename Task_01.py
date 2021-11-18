from time import sleep
""" Homework for the Lesson_05 """
""" Task 01 """
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    colors = ['Красный', 'Желтый', 'Зеленый']
    delay = [7, 2, 4]
    change_count = 5

    def __init__(self):
        self.__colors = 'Зеленый'

    def running(self):
        while True:
            try:
                self.change_count = int(input('Сколько раз светофор должен отработать полный цикл? : '))
                break
            except ValueError:
                print('Ожидаем целое число...')

        while self.change_count != 0:
            for i in self.colors:
                self.__colors = i
                print(f'Свет светофора: {self.__colors} ({self.delay[self.colors.index(self.__colors)]} сек.)')
                sleep(self.delay[self.colors.index(self.__colors)])
            self.change_count -= 1
        print('Светофор выключен')


TrafficLight = TrafficLight()
TrafficLight.running()
