N = int(input('Введите число '))
sum_elem = 0
for n in range(0, N):
    elem = (-1) ** n * (1 / 2 ** n)
    sum_elem += elem
    print('n =', n)
    print('elem = (−1) **', n, '* (½) **', n,  '=', elem)
print('Сумма равна:', sum_elem)
