from alunobib import Aluno
def main():
    matricula = input('Digite a matrícula do aluno: ')
    nome = input('Digite o nome do aluno: ')
    turma = input('Digite a turma do aluno: ')
    nota1 = float(input('Digite a nota 1 do aluno: '))
    nota2 = float(input('Digite a nota 2 do aluno: '))

    aluno = Aluno(matricula, nome, turma, nota1, nota2)

    print('\nDados do Aluno:')
    print(f'Matrícula: {aluno.matricula}')
    print(f'Nome: {aluno.nome}')
    print(f'Turma: {aluno.turma}')
    print(f'Nota 1: {aluno.boletim.nota1}')
    print(f'Nota 2: {aluno.boletim.nota2}')
    print(f'Média: {aluno.boletim.media}')

if __name__ == "__main__":
    main()