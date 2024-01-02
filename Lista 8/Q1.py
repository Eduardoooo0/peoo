def main():
  arquivo = open('alunos.txt','w')
  arquivo.close()
  while True:
    print('DIGITE:\n 1 - ADICIONAR ALUNO\n 2 - REMOVER ALUNO\n 3 - LISTAR ALUNOS\n 0 - SAIR')
    menu = int(input(':'))
    if menu == 0:
      print('fim do programa')
      break
    if menu == 1:
      addaluno()
    elif menu == 2:
      rmvaluno()
    elif menu == 3:
      listar()
def addaluno():
  arquivo = open('alunos.txt','r')
  mat = int(input('MATRÍCULA:'))
  nome = input('Nome:')
  nota = []
  soma = 0
  for i in range(4):
    notas = float(input(f'Nota {i+1}:'))
    nota.append(notas)
    soma += nota[i]
  media = soma / 4
  nota.append(media)
  arquivo = open('alunos.txt','a')
  arquivo.write(f'{mat} : {nome},{nota[0]},{nota[1]},{nota[2]},{nota[3]},{nota[4]}\n')
  arquivo.close()
  print('Aluno adicionado')
def converter():
    alunos = {}
    arquivo = open('alunos.txt','r')
    al = arquivo.readlines()
    arquivo.close()
    for i in range(len(al)):
        matricula = int(al[i].split(':')[0])
        lista = al[i].split(':')[1]
        lista1 = lista.replace('\n','')
        nome = lista1.split(',')[0]
        n1 = lista1.split(',')[1]
        n2 = lista1.split(',')[2]
        n3 = lista1.split(',')[3]
        n4 = lista1.split(',')[4]
        media = lista1.split(',')[5]
        alunos[matricula] = [nome,n1,n2,n3,n4,media]
    return alunos 
def rmvaluno():
   matricula = int(input('matrícula que você quer remover:'))
   remover = converter()
   if matricula not in remover.keys():
    print(f'Não Cadastrado!')
   else:
    remover.pop(matricula)
    arquivo = open('alunos.txt','w')
    arquivo.close()
    for matricula,lista in remover.items():
        arquivo = open('alunos.txt','a')            
        arquivo.writelines(f'{matricula}:{lista[0]},{lista[1]},{lista[2]},{lista[3]},{lista[4]}\n')
    arquivo.close()
def listar():
  arquivo = open('alunos.txt','r')
  ltr = arquivo.readlines()
  for i in range(len(ltr)):
    print(f'aluno {i}: {ltr[i]}')
if __name__ == '__main__':
    main()