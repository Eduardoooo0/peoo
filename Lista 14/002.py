from tkinter import *
import requests
import json
class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Lista 12 - Questão 02')
        self.janela.geometry("470x440")
        self.janela.resizable(width = False, height = False)

        self.Label1 = Label(background = 'white', font = 'Arial 22 bold', foreground = 'gray', text = 'Consulta DDD e Cidade')
        self.Label1.place(x = 11, y = 11, height = 43, width = 446, anchor = 'nw')
        self.Label2 = Label(font = 'Arial 20', text = 'Informe o DDD a Consultar:')
        self.Label2.place(x = 8, y = 66, height = 30, width = 344, anchor = 'nw')
        self.Entry1 = Entry(borderwidth = 3, font = 'Arial 22 bold', foreground = 'blue', justify = 'center')
        self.Entry1.place(x = 354, y = 63, height = 37, width = 56, anchor = 'nw')
        self.Button1 = Button(background = 'blue', font = 'Arial 22 bold', foreground = 'white', text = 'Consultar DDD',command=self.Consultar)
        self.Button1.place(x = 10, y = 111, height = 48, width = 449, anchor = 'nw')
        self.Label3 = Label(font = 'Arial 20 bold', text = 'Estado do DDD:')
        self.Label3.place(x = 15, y = 186, height = 30, width = 281, anchor = 'nw')
        self.Label4 = Label(background = 'gray', font = 'Arial 20 bold', text = '')
        self.Label4.place(x = 260, y = 178, height = 43, width = 175, anchor = 'nw')
        self.Label5 = Label(font = 'Arial 16', text = 'Cidade a Consultar:')
        self.Label5.place(x = 9, y = 256, height = 30, width = 209, anchor = 'nw')
        self.Entry2 = Entry(borderwidth = 3,font = 'Arial 22 bold', foreground = 'blue')
        self.Entry2.place(x = 214, y = 250, height = 38, width = 245, anchor = 'nw')
        self.Button2 = Button(background = 'blue', font = 'Arial 20 bold', foreground = 'white', text = 'Consultar Cidade',command=self.Cidade)
        self.Button2.place(x = 15, y = 303, height = 42, width = 441, anchor = 'nw')
        self.LabelFrame1 = LabelFrame(text = 'Resposta à Consulta')
        self.LabelFrame1.place(x = 21, y = 352, height = 78, width = 433,anchor = 'nw')
        self.Label6 = Label(background = 'gray', font = 'Arial 14 bold', text = 'Aguardando informações para consultar')
        self.Label6.place(x = 30, y = 379, height = 30, width = 414, anchor = 'nw')

        self.janela.mainloop()
    def Consultar(self):
      self.ddd = self.Entry1.get()
      self.consulta = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{self.ddd}')
      if self.consulta.status_code == 200:
        self.uf = self.consulta.json()["state"]
        self.Label4.config(text=self.uf)
        self.Label6.config(text='Aguardando cidade a consultar')
      else:
        self.Label6.config(text='DDD não encontrado')
    def Cidade(self):
      self.ddd = self.Entry1.get()
      self.consulta = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{self.ddd}')
      self.cidade = self.Entry2.get()
      self.city = self.consulta.json()["cities"] 
      if self.cidade.upper() in self.city:
        self.Label6.config(text=' Cidade PERTENCE à área do DDD')
      else:
        self.Label6.config(text='Cidade não pertence à área do DDD')





aplicacao=App()