from tkinter import *
from random import shuffle
from datetime import datetime

def sort():

    members = [member.get() for member in membro]

    resultado = Tk()
    resultado.title('Resultado')

    currentTime = datetime.now()

    aux=[]
    rotulo = []

    aux.append("%s \n\nTempo total da rodada:\n %d min\n" %(currentTime.strftime("%d/%m/%Y %H:%M:%S"), len(members)*10))
    rotulo.append(Label(resultado, text=aux[0]).grid(row=0, column=0))

    shuffle(members)

    for i in range(1,len(members)):
        aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(i,members[i-1],members[i]))
        rotulo.append(Label(resultado, text=aux[i]).grid(row=i, column=0))
        if (i==len(members)-1) :
            aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(len(members),members[len(members)-1],members[0]))
            rotulo.append(Label(resultado, text=aux[len(members)]).grid(row=len(members), column=0))

def contar():
    # Instancia a janela:

    sorteio = Tk()
    sorteio.title('Sorteio CD Py')


    n = int(number.get())

    # Instancia os rotulos usando a classe Label e os coloca na janela usando o gerenciador de layout 'grid'
    rotulos=[]
    for i in range(n):
        rotulos.append(Label(sorteio, text='Membro '+str(i+1)+': ').grid(row=i, column=0))

    # Usa a classe Entry para criar as caixas de texto e em seguida as coloca na janela com o gerenciador de layout 'grid'

    global membro
    membro = list()
    for i in range(n):
        membro.append(Entry(sorteio))
        membro[i].grid(row=i, column=1)

    sairBotao = Button(sorteio, text='Sair', command=sorteio.quit).grid(row=len(rotulos), column=0, sticky=W, pady=4)
    sortearBotao = Button(sorteio, text='Fazer sorteio', command=sort).grid(row=len(rotulos), column=1, sticky=W, pady=4)

start = Tk()

rotulo = Label(start, text='Numero de integrantes: ')
rotulo.grid(row=0, column=0)

number = Entry(start)
number.grid(row=0, column=1)

sairBotao = Button(start, text='Sair', command=start.quit).grid(row=1, column=0, sticky=W, pady=4)
contarBotao = Button(start, text='Prosseguir', command = contar).grid(row=1, column=1, sticky=W, pady=4)

start.title('Sorteio CD Py')
start.mainloop()