s  = input('digite algo:').upper()
fsp = s.replace(',','  ').replace('.','  ').replace(';',' ').replace('?',' ').replace('!',' ')
num = fsp.split()
print(f'a frase tem {len(num)} palavras ')
