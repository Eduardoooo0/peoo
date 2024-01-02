lista = []
lista2 = []
soma = ''
num = int(input('digite um número maior que 1000:'))
num = str(num)
for i in num:
    lista.append(i)
lista.sort(reverse=True)
for i in lista:
    soma += i
num = int(soma)
print(num + 1000)
