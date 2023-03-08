boy = int(input('Введите число мальчиков '))
girls = int(input('Введите число девочек '))
string = ""
for i in range(1, boy+1):
    i = "B"
    for j in  range(1, girls+1):
        j = "G"
    string += i + j
print(string)

