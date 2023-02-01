import tkinter as tk
from tkinter import ttk
from tkinter import *

# cores
cor1 = "#050505" #preto
cor2 = "#aef5ef" #azul fundo painel ( digitos )
cor3 = "#ab6597" #azul escuro botoes laterais
cor4 = "#cf78cd" #azul claro fundo
cor5 = "#5589bd" #botoes
cor6 = "#ffffff" #rosa
janela = Tk()
janela.title('Calculadora')
janela.geometry("360x310")
janela.config(bg=cor4)

#criando frames
frame_tela = Frame(janela, width=360, height=50, bg=cor1)
frame_tela.grid(row=0, columns=1)

frame_faixa = Frame(janela, width=360, height=5, bg=cor6)
frame_faixa.grid(row=1, columns=1)

frame_botoes = Frame(janela, width=360, height=450, bg=cor5)
frame_botoes.grid(row=2, columns=1)

#variavel todos valores
todos_valores = ''
imputdousuario = StringVar()


#funcao calcular
def entra_valores(evento):
    global todos_valores
    todos_valores = todos_valores + str(evento)

    #Passando valores para o visor
    imputdousuario.set(todos_valores)

#funcao para calcular
def calcular ():
    global todos_valores
    resultado = eval(todos_valores)
    imputdousuario.set(resultado)

def limpar_tela():
    global todos_valores
    todos_valores =''
    imputdousuario.set('')




#criando labels

visor = Label(frame_tela, textvariable=imputdousuario, width=24, height=2, relief=FLAT, anchor="e", padx=2, pady=1, bg=cor1,fg=cor2, font=('Gadugi 18 bold'))
visor.place(x=1, y=1)



#criando Botoes linha 1
bt1 = Button(frame_botoes, command=limpar_tela, text= "Limpar", width=18, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=3, y=5)
bt2 = Button(frame_botoes, command=lambda: entra_valores('%'), text= "%", width=8, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=185, y=5)
bt3 = Button(frame_botoes, command=lambda: entra_valores('/'), text= "÷", width=8, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=275, y=5)

#2 linha de botoes
bt4 = Button(frame_botoes, command=lambda: entra_valores('7'), text= "7", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=5, y=60)
bt5 = Button(frame_botoes, command=lambda: entra_valores('8'), text= "8", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=95, y=60)
bt6 = Button(frame_botoes, command=lambda: entra_valores('9'), text= "9", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=185, y=60)
bt7 = Button(frame_botoes, command=lambda: entra_valores('*'), text= "x", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=275, y=60)

#3 linha botoes
bt4 = Button(frame_botoes, command=lambda: entra_valores('4'), text= "4", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=5, y=105)
bt5 = Button(frame_botoes, command=lambda: entra_valores('5'), text= "5", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=95, y=105)
bt6 = Button(frame_botoes, command=lambda: entra_valores('6'), text= "6", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=185, y=105)
bt7 = Button(frame_botoes, command=lambda: entra_valores('-'), text= "-", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=275, y=105)

#3 linha botoes
bt4 = Button(frame_botoes, command=lambda: entra_valores('1'), text= "1", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=5, y=150)
bt5 = Button(frame_botoes, command=lambda: entra_valores('2'), text= "2", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=95, y=150)
bt6 = Button(frame_botoes, command=lambda: entra_valores('3'), text= "3", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=185, y=150)
bt7 = Button(frame_botoes, command=lambda: entra_valores('+'), text= "+", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=275, y=150)

#4 linha botoes
bt4 = Button(frame_botoes, command=lambda: entra_valores('0'), text= "+/-", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=5, y=195)
bt5 = Button(frame_botoes, command=lambda: entra_valores('0'), text= "0", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=95, y=195)
bt6 = Button(frame_botoes, command=lambda: entra_valores(','), text= ",", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=185, y=195)
bt7 = Button(frame_botoes, command=calcular, text="=", width=9, height=2, font=('Verdana 10 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=275, y=195)


janela.mainloop()
