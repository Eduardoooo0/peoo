alunos = {}
alunos_apv = {}
matricula = 1
while not matricula == 0:
  matricula = int(input('MATRICULA:'))
  if matricula == 0:
    break
  else:
    lista = []
    nome = input('NOME DO ALUNO:')
    nota1 = float(input('NOTA 1:'))
    nota2 = float(input('NOTA 2:'))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    alunos.update({matricula:lista})
    print()
print()
print(f'* Número de alunos matriculados: {len(alunos.keys())}')
lista_nome = []
soma1 = soma2 = somat = 0
for v,i in alunos.items():
  lista_nome.append(i[0])
  soma1 += i[1]
  soma2 += i[2]
  somat += i[1] + i[2]
  if somat/len(alunos.keys()) >= 120:
    alunos_apv.update({v:i[0]})
print(f'* Nome dos Alunos:{lista_nome}')
media1 = soma1/len(alunos.keys())
print(f'* Média das notas 1: {media1}')
media2 = soma2/len(alunos.keys())
print(f'* Média das notas 2: {media2}')
mediat = somat/len(alunos.keys())
print(f'* Média Total: {mediat}')
for m,n in alunos_apv.items():
  print(f'* Aluno: {n} | Matricula: {m} | Aprovado')