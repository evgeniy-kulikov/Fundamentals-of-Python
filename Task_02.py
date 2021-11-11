""" Task 02 """
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
num_second = int(input('Введите количество секунд: '))
whole_sec = num_second % 60
whole_min = num_second // 60 % 60
whole_hour = num_second // 3_600 % 60
whole_hour_day = num_second // 3_600 % 60 % 24
whole_day = num_second // 86_400 % 24
# Вывод в формате чч:мм:сс
if num_second < 86400:
    print(f'{whole_hour:02}:{whole_min:02}:{whole_sec:02}')
# Вывод в формате дд.чч:мм:сс
else:
    print(f'{whole_day:02}:{whole_hour_day:02}:{whole_min:02}:{whole_sec:02}')
