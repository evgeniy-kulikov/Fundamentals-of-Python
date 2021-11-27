
""" Homework for the Lesson_08 """
""" Task 07 """

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return f'{self.real}{sign}{self.imag}i'


class ComplexCalc:
    def add(self, c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return Complex(real, imag)

    def sub(self, c1, c2):
        real = c1.real - c2.real
        imag = c1.imag - c2.imag
        return Complex(real, imag)

    def mul(self, c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        return Complex(real, imag)


z_1 = Complex(1, -2)
z_2 = Complex(3, 4)
print(f'первое комплексное число z1: {z_1}')
print(f'второе комплексное число z2: {z_2}')
calc = ComplexCalc()
print(f'Сумма z1 и z2 равна: {calc.add(Complex(1, -2), Complex(3, 4))}')
print(f'Разность z1 и z2 равна: {calc.sub(Complex(1, -2), Complex(3, 4))}')
print(f'Произведение z1 и z2 равно: {calc.mul(Complex(1, -2), Complex(3, 4))}')


print('\nПроверка с использованием встроенного модуля "cmath" ')
print(f'z1 = {complex(1, -2)}')
print(f'z2 = {complex(3, 4)}')
print(f'Сумма z1 и z2 равна: {complex(1, -2) + complex(3, 4)}')
print(f'Разность z1 и z2 равна: {complex(1, -2) - complex(3, 4)}')
print(f'СПроизведение z1 и z2 равно: {complex(1, -2) * complex(3, 4)}')
