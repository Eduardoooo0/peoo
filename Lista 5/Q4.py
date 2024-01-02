lista = []
lista2 = []
cont = 0
s  = input('digite algo:').upper()
for i in s:
    lista2.append(i)
for i in range(0,len(s)):
    num = s.count(lista2[i])
    lista.append(num)
    cont += 1
    if cont == 1:
        print(f'{lista2[i]} = {lista[i]} vezes')
    else:
        print(f'{lista2[i]} = {lista[i]} vezes')
