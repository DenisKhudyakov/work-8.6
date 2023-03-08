# Задание № 1
month = int(input('Введите количество месяцев: '))
weight = 100
for i in range(1, month+1):
    weight -= 4
print('Осталось гречки:', weight, 'кг')
