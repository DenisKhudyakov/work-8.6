# Задачка 6
educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
summ_deficit = 0
print('Месяц траты', expenses, 'не хватает', expenses - educational_grant)
for i in range(1, 10):
    deficit = (expenses - educational_grant)
    summ_deficit += deficit
    expenses += expenses * 0.03
    print('Месяц траты', '%.2f' % expenses, 'не хватает', '%.2f' % ((expenses - educational_grant) + summ_deficit))



