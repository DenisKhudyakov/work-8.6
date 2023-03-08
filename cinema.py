boy = int(input('Введите число мальчиков '))
girls = int(input('Введите число девочек '))
string = ""
if boy / girls >= 2 or girls / boy >=2:
    print('Не получится усадить их по ТЗ')
elif boy >= girls:
    k = boy - girls
    for x in range(k):
        string += 'BGB'
    for y in range(girls - k):
        string += 'BG'
else:
    k = girls - boy
    for z in range(k):
        string += 'GBG'
    for d in range(boy - k):
        string += 'GB'
print(string)
