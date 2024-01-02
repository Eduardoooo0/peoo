lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','dezembro']
data = input('digite sua data de nascimento ss/mm/aaaa:')
data = data.split('/')
d1 = data[0]
d2 = int(data[1])
d3 = data[2]
print(f'{d1} {lista[d2-1]} {d3}')


