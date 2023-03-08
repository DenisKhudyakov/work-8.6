#Задание №2
debtor = int(input('Введите количество должников: '))
sum_debt = 0
for i in range(0, debtor+1, 5):
    print('Должник с номером', i)
    debt = int(input('Сколько денег вы должны: '))
    sum_debt += debt
print('Общая сумма долга', sum_debt, 'руб')

