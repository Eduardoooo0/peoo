valor = float(input('digite o valor das compras:'))
pix = valor * (3/100)
total = valor - pix
print(f'você pagará R${total} por ter um desconto de R${pix}')