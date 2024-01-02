class Notas:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = self.calcular_media()

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2


class Aluno:
    def __init__(self, matricula, nome, turma, nota1, nota2):
        self.matricula = matricula
        self.nome = nome
        self.turma = turma
        self.boletim = Notas(nota1, nota2)