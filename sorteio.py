from tkinter import *
from random import shuffle

def sort(members):

    aux=[]
    aux.append("Tempo total da rodada: %d min\n" %(len(members)*10))
    rotulo = []
    rotulo.append(Label(resultado, text=aux[0]).grid(row=0, column=0))

    shuffle(members)

    for i in range(1,len(members)):
        aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(i,members[i-1],members[i]))
        rotulo.append(Label(resultado, text=aux[i]).grid(row=i, column=0))
        if (i==len(members)-1) :
            aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(len(members),members[len(members)-1],members[0]))
            rotulo.append(Label(resultado, text=aux[len(members)]).grid(row=len(members), column=0))


def sortear():
   membros = [member.get() for member in membro]
   sort(membros)

# Instancia a janela:

janela = Tk()
resultado = Tk()

# Numero de pessoas a sortear:
n = 5

# Instancia os rótulos usando a classe Label e os coloca na janela usando o gerenciador de layout 'grid'
rotulos=[]
for i in range(n):
    rotulos.append(Label(janela, text='Membro '+str(i+1)+': ').grid(row=i, column=0))

# Usa a classe Entry para criar as caixas de texto e em seguida as coloca na janela com o gerenciador de layout 'grid'

membro = []
for i in range(n):
    membro.append(Entry(janela))
    membro[i].grid(row=i, column=1)

sairBotao = Button(janela, text='Sair', command=janela.quit).grid(row=len(rotulos), column=0, sticky=W, pady=4)
sortearBotao = Button(janela, text='Fazer sorteio', command=sortear).grid(row=len(rotulos), column=1, sticky=W, pady=4)

janela.title('Sorteio CD Py')
resultado.title('Resultado')
janela.mainloop()