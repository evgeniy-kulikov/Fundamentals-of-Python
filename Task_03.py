""" Task 03 """
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
num_user = input('Введите целое число: ')
num_2 = num_user * 2
num_3 = num_user * 3
num_sum = int(num_user) + int(num_2) + int(num_3)
print(f'{num_user} + {num_2} + {num_3} = {num_sum}')
