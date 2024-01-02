frase = input('digite uma frase:')
esp = frase.count(' ')
cont = 0
for i in frase:
    if i in 'aeiou':
        cont += 1
print(f'{esp} espaços e {cont} vogais')