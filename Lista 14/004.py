from tkinter import *
import sqlite3 as sql

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Escola internacional')
        self.janela.geometry('600x400')
        self.janela.eval('tk::PlaceWindow . center')
        self.janela.resizable(width = False, height = False)
        self.metodo = ''
        self.nome = ''
        self.canva = Canvas(self.janela, bg='gray')
        self.canva.place(x=0, y=4, height=600, width=600)
        self.Label1 = Label(self.janela, text = 'Escola internacional', background = 'Black', borderwidth = 2, font = 'Arial 25 bold', foreground = 'White')
        self.Label1.place(x = 0, y = 4, height = 50, width = 597)
        self.Label2 = Label(self.canva, text = 'Escolha uma opção:', background='gray', font = 'Arial 15 bold')
        self.Label2.place(x = 15, y = 50, height = 50)
        self.entry=''
        self.botao1 = Button(self.canva,text='Inserir aluno',font=('Arial', 10), background='green', foreground='White', borderwidth=3,command=self.Inserir)
        self.botao1.place(x=420,y=60,height=50,width=150)
        self.botao2 = Button(self.canva,text='Excluir aluno',font=('Arial', 10), background='red', foreground='White', borderwidth=3,command=self.Excluir)
        self.botao2.place(x=420,y=120,height=50,width=150)
        self.botao3 = Button(self.canva,text='Inserir/alterar notas',font=('Arial', 10), foreground='black', borderwidth=3,command=self.Nota)
        self.botao3.place(x=420,y=180,height=50,width=150)
        self.botao4 = Button(self.canva,text='Listar Aprovados',font=('Arial', 10),foreground='black', borderwidth=3,command=self.Aprovados)
        self.botao4.place(x=420,y=240,height=50,width=150)
        self.botao5 = Button(self.canva,text='OK',font=('Arial', 10), foreground='black', borderwidth=3,command=self.Ok)
        self.botao5.place(x=420,y=300,height=50,width=150)
        self.labeln1 = Label(self.canva, text = 'Nota 1:', background='gray', font = 'Arial 15 bold')
        self.labeln1.place(x=0, y=175, height=50, width=100)
        self.nota1 = Entry(self.canva, font = 'Arial 15 bold')
        self.nota1.place(x=95, y=185, height=30, width=50)
        self.labeln2 = Label(self.canva, text = 'Nota 2:', background='gray', font = 'Arial 15 bold')
        self.labeln2.place(x=145, y=175, height=50, width=100)
        self.nota2 = Entry(self.canva, font = 'Arial 15 bold')
        self.nota2.place(x=240, y=185, height=30, width=50)
        self.labeln3 = Label(self.canva, text = 'Nota 3:', background='gray', font = 'Arial 15 bold')
        self.labeln3.place(x=0, y=220, height=50, width=100)
        self.nota3 = Entry(self.canva, font = 'Arial 15 bold')
        self.nota3.place(x=95, y=230, height=30, width=50)
        self.labeln4 = Label(self.canva, text = 'Nota 4:', background='gray', font = 'Arial 15 bold')
        self.labeln4.place(x=145, y=220, height=50, width=100)
        self.nota4 = Entry(self.canva, font = 'Arial 15 bold')
        self.nota4.place(x=240, y=230, height=30, width=50)
        self.janela.mainloop()
    def Inserir(self):
      self.metodo = 'Inserir'
      self.Label2.config(text='Digite o nome do aluno a inserir:',foreground='black')
      self.entry = Entry(self.canva, font = 'Arial 15 bold')
      self.entry.place(x=15, y=100, height=50, width=350)
    def Excluir(self):
      self.metodo = 'Excluir'
      self.Label2.config(text='Digite o nome do aluno a excluir:',foreground='black')
      self.entry = Entry(self.canva, font = 'Arial 15 bold')
      self.entry.place(x=15, y=100, height=50, width=350)
    def Nota(self):
      self.metodo = 'Nota'
      self.Label2.config(text='Nome do aluno para Inserir/Alterar notas:',foreground='black')
      self.entry = Entry(self.canva, font = 'Arial 15 bold')
      self.entry.place(x=15, y=100, height=50, width=350)
    def Aprovados(self):
      self.metodo = 'Aprovados'
    def Ok(self):
      if self.metodo == 'Inserir':
        self.nome = self.entry.get()
        self.con = sql.connect('Banco.db')
        self.sql = self.con.cursor()
        self.sql.execute(f'INSERT INTO alunos (nome) VALUES ("{self.nome}")')
        self.con.commit()
        self.con.close()
        self.Label2.config(text='Aluno cadastrado com sucesso!',foreground='green')
        self.entry = Label(self.canva, text='',background='gray')
        self.entry.place(x=15, y=100, height=50, width=350)
        self.metodo = ''

      if self.metodo == 'Excluir':
        self.nome = self.entry.get()
        self.con = sql.connect('Banco.db')
        self.sql = self.con.cursor()
        self.sql.execute('SELECT * FROM alunos')
        self.registros = self.sql.fetchall()
        for i in self.registros:
            if self.nome in i:
                self.sql.execute(f"DELETE FROM alunos WHERE nome='{self.nome}'")
                self.con.commit()
                self.con.close()
                self.Label2.config(text='Aluno excluido com sucesso!',foreground='red')
                self.entry = Label(self.canva, text='',background='gray')
                self.entry.place(x=15, y=100, height=50, width=350)
                self.metodo = ''
            else:
                self.Label2.config(text='Aluno não encontrado!',foreground='red')
      if self.metodo == 'Nota':
        self.nome = self.entry.get()
        self.con = sql.connect('Banco.db')
        self.sql = self.con.cursor()
        self.sql.execute('SELECT * FROM alunos')
        self.registros = self.sql.fetchall()
        for i in self.registros:
            if self.nome in i:
                self.lista = [self.nota1.get(),self.nota2.get(), self.nota3.get(),self.nota4.get()]
                self.sql.execute(f"UPDATE alunos SET nota1='{self.lista[0]}' WHERE nome='{self.nome}'")
                self.sql.execute(f"UPDATE alunos SET nota2='{self.lista[1]}' WHERE nome='{self.nome}'")
                self.sql.execute(f"UPDATE alunos SET nota3='{self.lista[2]}' WHERE nome='{self.nome}'")
                self.sql.execute(f"UPDATE alunos SET nota4='{self.lista[3]}' WHERE nome='{self.nome}'")
                self.con.commit()
                self.con.close()
                self.Label2.config(text='Notas adiconadas com sucesso!',foreground='green')
            else:
                self.Label2.config(text='Aluno não encontrado!',foreground='red')
        self.entry = Label(self.canva, text='',background='gray')
        self.entry.place(x=15, y=100, height=50, width=350)
        self.nota1.delete(0,END)
        self.nota2.delete(0,END)
        self.nota3.delete(0,END)
        self.nota4.delete(0,END)
        self.metodo = ''
      if self.metodo == 'Aprovados':
        self.metodo = 'Aprovados'
        self.con = sql.connect('Banco.db')
        self.sql = self.con.cursor()
        self.sql.execute('SELECT nome, nota1, nota2, nota3, nota4 FROM alunos')
        self.registros = self.sql.fetchall()
        self.alunos_aprovados = []

        for aluno in self.registros:
            nome, nota1, nota2, nota3, nota4 = aluno
            media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

            if media >= 60:
                self.alunos_aprovados.append(nome)

        self.con.close()

        for nome_aprovado in self.alunos_aprovados:
            print(nome_aprovado)
aplicacao=App()