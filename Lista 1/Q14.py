produto = float(input('digite o valor da mercadoria:'))
desconto = int(input('quantos porcentos de desconto?:'))
p_total = produto * (desconto/100)
p_total = produto - p_total
print(f'a mercadoria custava R${produto} e com {desconto}% de desconto ficou R${p_total}')