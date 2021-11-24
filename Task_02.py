from abc import ABC, abstractmethod
""" Homework for the Lesson_07 """
""" Task 02 """

# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes(ABC):  # родительский класс (для Coat & Suit) создается на базе абстрактного класса
    @abstractmethod
    def expense(self):  # функция вычисления (будет переопределена в дочерних классах)
        pass


class Coat(Clothes):  # пальто
    def __init__(self, v):
        self.v = v  # размер пальто

    @property
    def expense(self):  # переопределяем метод "expense" класса "Clothes"
        return self.v / 6.5 + 0.5  # расход ткани на одно пальто (заданного размера)

    def sum_exp_coat(self, sum_coat):  # общий расход ткани партии пальто
        num = 0  # начальное значение счетчика пальто
        for coat in sum_coat:
            num += coat.expense
        return num


class Suit(Clothes):  # костюм
    def __init__(self, h):
        self.h = h  # рост костюма

    @property
    def expense(self):  # переопределяем метод "expense" класса "Clothes"
        return self.h * 2 + 0.3  # расход ткани на один костюм (заданного роста)

    def sum_expense(self, sum_suit):  # общий расход ткани партии костюмов
        num = 0  # начальное значение счетчика костюмов
        for suit in sum_suit:
            num += suit.expense
        return num


suit_1 = Suit(1.54)
suit_2 = Suit(1.68)
suit_3 = Suit(1.76)
suit_4 = Suit(1.94)
sum_unit = [suit_1, suit_2, suit_3, suit_4]
print(f'Расход ткани на один костюм (рост {suit_1.h}): {round(suit_1.expense, 2)} кв.м')
print(f'Расход ткани на партию костюмов: {round(suit_1.sum_expense(sum_unit), 2)}\n')
coat_1 = Coat(46)
coat_2 = Coat(48)
coat_3 = Coat(50)
coat_4 = Coat(52)
sum_coat = [coat_1, coat_2, coat_3, coat_4]
print(f'Расход ткани на одно пальто (размер {coat_1.v}) {round(coat_1.expense, 2)} кв.м')
print(f'Расход ткани на партию пальто: {round(coat_1.sum_exp_coat(sum_coat), 2)}')
