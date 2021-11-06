"""Homework for the Lesson_03"""

""" Task 06 """
#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#  но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(up_text):
    upper_str = chr(ord(up_text[0]) - 32) + up_text[1:]
    return upper_str


user_text = input('Введите слово из строчных букв: ')
out_text = int_func(user_text)
print(out_text)

# 6.2 Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

str_upper = []
user_srt = input('Введите строку из строчных букв: ').split()
for i in range(len(user_srt)):
    str_upper.append(int_func(user_srt[i]))
print(' '.join(str_upper))
