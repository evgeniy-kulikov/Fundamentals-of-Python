""" Homework for the Lesson_08 """
""" Task 02 """

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyError(Exception):
    def __init__(self, text):
        self.txt = text  # в переменную "text" выводится нужное сообщение об ошибке


numerator = input('Введие делимое число: ')
denominator = input('Введие делитель для этого числа: ')

try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
        raise MyError("на ноль делить нельзя!")  # возбуждаем исключение с передачей нужного текста ошибки
except ValueError:
    print("Необходимо ввести число!")  # проверка на ввод чисел
except MyError as user_mistake:  # в переменную "user_mistake" передаем срабатывание для класса  "MyError"
    print(f'Ошибка: {user_mistake}')
else:
    print(numerator / denominator)
