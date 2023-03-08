a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
sum_num = 0
d = 0
for i in range(a, b, c):
    sum_num += i
    d += 1
print('Среднее арифметическое отрезка a и b =', sum_num / d)