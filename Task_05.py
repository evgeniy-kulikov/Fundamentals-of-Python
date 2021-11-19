""" Homework for the Lesson_05 """
""" Task 05 """

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


# Создаем дочерние классы и переопределяем в них метод "draw"
class Pen(Stationary):

    def draw(self):
        return f'Выбрана "{self.title}". Запуск отрисовки ручкой'


class Pencil(Stationary):

    def draw(self):
        return f'Выбран "{self.title}". Запуск отрисовки карандашом'


class Handle(Stationary):

    def draw(self):
        return f'Выбран "{self.title}". Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
