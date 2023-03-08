#Задание № 3
reverse_timer = int(input('Введите время: '))
for sec in range(reverse_timer, -1, -1):
    if sec > 60:
        print(sec // 60, 'мин', sec % 60, 'сек')
    else:
        print(sec, 'сек')
    message = int(input('Готовы ли вы забрать еду? '))
    if message == 1:
        print('«Да, еда готова»')
        break
#    elif message == 0:
#        continue
print('«Ваша еда готова, осторожно горячo!»')





