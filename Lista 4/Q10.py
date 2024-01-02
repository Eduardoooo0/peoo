lista = []
while True:
    num = int(input('digite um  número:'))
    if num == 0:
        break
    else:
        lista.append(num)
soma = ''
for i in lista:
    num = i
    num = str(num)
    soma += num
num = int(soma)
print(num)

