from tkinter import *
class Calculadora:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('320x280')
        self.janela.title('Calculadora')
        self.canvas1 = Canvas(self.janela, bg='gray', height=280, width=320)
        self.canvas1.pack()
        self.imagem = PhotoImage(file='logo_ifrn_01.png').subsample(15)
        self.imagemexibir = self.canvas1.create_image(40,50,image=self.imagem)
        

        self.resultado = Label(self.canvas1,text='0.00',font=('arial',25),anchor='e')
        self.resultado.place(x=80,y=10,height=80,width=225)

        self.botao7 = Button(self.canvas1,pady=5,text='7',command= lambda: self.adc_num('7'))
        self.botao7.place(x=20,y=105,width=50,height=30)

        self.botao8 = Button(self.canvas1,text='8',command= lambda: self.adc_num('8'))
        self.botao8.place(x=75,y=105,width=50,height=30)

        self.botao9 = Button(self.canvas1,text='9',command= lambda: self.adc_num('9'))
        self.botao9.place(x=130,y=105,width=50,height=30)

        self.botaomais = Button(self.canvas1,text='+',command= lambda: self.adc_opr('+'))
        self.botaomais.place(x=185,y=105,width=50,height=30)

        self.botaoseta = Button(self.canvas1,text='←',bg='red',command= lambda: self.deletar())
        self.botaoseta.place(x=240,y=105,width=70,height=30)

        self.botaoigual = Button(self.canvas1,text='=',bg='black',fg='white',command=lambda:self.calcular())
        self.botaoigual.place(x=240,y=140,width=70,height=100)

        self.botao4 = Button(self.canvas1,pady=5,text='4',command= lambda: self.adc_num('4'))
        self.botao4.place(x=20,y=140,width=50,height=30)

        self.botao5 = Button(self.canvas1,text='5',command= lambda: self.adc_num('5'))
        self.botao5.place(x=75,y=140,width=50,height=30)

        self.botao6 = Button(self.canvas1,text='6',command= lambda: self.adc_num('6'))
        self.botao6.place(x=130,y=140,width=50,height=30)

        self.botaomenos = Button(self.canvas1,text='-',command= lambda: self.adc_opr('-'))
        self.botaomenos.place(x=185,y=140,width=50,height=30)

        self.botao1 = Button(self.canvas1,pady=5,text='1',command= lambda: self.adc_num('1'))
        self.botao1.place(x=20,y=175,width=50,height=30)

        self.botao2 = Button(self.canvas1,text='2',command= lambda: self.adc_num('2'))
        self.botao2.place(x=75,y=175,width=50,height=30)

        self.botao3 = Button(self.canvas1,text='3',command= lambda: self.adc_num('3'))
        self.botao3.place(x=130,y=175,width=50,height=30)

        self.botaodiv = Button(self.canvas1,text='/',command= lambda: self.adc_opr('/'))
        self.botaodiv.place(x=185,y=175,width=50,height=30)

        self.botao0 = Button(self.canvas1,pady=5,text='0',command= lambda: self.adc_num('0'))
        self.botao0.place(x=20,y=210,width=50,height=30)

        self.botaoponto = Button(self.canvas1,text='.')
        self.botaoponto.place(x=75,y=210,width=50,height=30)

        self.botaoc = Button(self.canvas1,text='C',bg='yellow',command= lambda: self.limpar())
        self.botaoc.place(x=130,y=210,width=50,height=30)

        self.botaomult = Button(self.canvas1,text='*',command= lambda: self.adc_opr('*'))
        self.botaomult.place(x=185,y=210,width=50,height=30)

        self.texto = self.canvas1.create_text(260,260,text='Lista 12',font=('arial',20))
        self.canvas1.itemconfig(self.texto,fill='white')
        self.canvas1.tag_bind(self.imagemexibir,'<Button-1>',self.mudar)

        self.janela.mainloop()
    def adc_num(self,numero):
        self.num_atual = self.resultado['text']

        if self.num_atual == '0.00':
            self.resultado['text'] = numero
        else:
            self.resultado['text'] = self.resultado['text'] + numero
    def adc_opr(self,operador):
        self.resultado_atual = self.resultado['text']
        if self.resultado_atual[-1] not in ['+','-','*','/']:
            self.resultado['text'] = self.resultado_atual + operador
    def limpar(self):
        self.resultado['text'] = '0.00'
    def deletar(self):
        self.resultado_atual = self.resultado['text']
        self.resultado['text'] = self.resultado_atual[:-1]
    def calcular(self):
        resultado_atual = self.resultado['text']
        try:
            resultado = eval(resultado_atual)
            self.resultado['text'] = str(resultado)
        except:
            self.resultado['text'] = 'Erro'
    def mudar(self,evento):
        self.coratual = self.botaoigual['bg']
        if self.coratual == 'black':
            self.botaoigual = Button(self.canvas1,text='=',bg='blue',fg='white',command=lambda:self.calcular())
            self.botaoigual.place(x=240,y=140,width=70,height=100)
        else:
            self.botaoigual = Button(self.canvas1,text='=',bg='black',fg='white',command=lambda:self.calcular())
            self.botaoigual.place(x=240,y=140,width=70,height=100)


