from tkinter import *
from random import shuffle

def sort(members):

    aux=[]
    aux.append("Tempo total da rodada: %d min\n" %(len(members)*10))

    shuffle(members)

    for i in range(1,len(members)):
        aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(i,members[i-1],members[i]))
        if (i==len(members)-1) :
            aux.append("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(len(members),members[len(members)-1],members[0]))

    rotulo6['text'] = aux


def sortear():
   membros = [membro1.get(), membro2.get(), membro3.get(), membro4.get(), membro5.get()]
   sort(membros)

# Instancia a janela:

janela = Tk()

# Instancia os rótulos usando a classe Label e os coloca na janela usando o gerenciador de layout 'grid'

rotulo1 = Label(janela, text="Membro 1: ")
rotulo1.grid(row=0, column=0)
rotulo2 = Label(janela, text="Membro 2: ")
rotulo2.grid(row=1, column=0)
rotulo3 = Label(janela, text="Membro 3: ")
rotulo3.grid(row=2, column=0)
rotulo4 = Label(janela, text="Membro 4: ")
rotulo4.grid(row=3, column=0)
rotulo5 = Label(janela, text="Membro 5: ")
rotulo5.grid(row=4, column=0)
rotulo6 = Label(janela, text='')
rotulo6.grid(row=6, column=1)

# Usa a classe Entry para criar as caixas de texto e em seguida as coloca na janela com o gerenciador de layout 'grid'

membro1 = Entry(janela)
membro1.grid(row=0, column=1)
membro2 = Entry(janela)
membro2.grid(row=1, column=1)
membro3 = Entry(janela)
membro3.grid(row=2, column=1)
membro4 = Entry(janela)
membro4.grid(row=3, column=1)
membro5 = Entry(janela)
membro5.grid(row=4, column=1)

sairBotao = Button(janela, text='Sair', command=janela.quit)
sairBotao.grid(row=5, column=0, sticky=W, pady=4)
sortearBotao = Button(janela, text='Fazer sorteio', command=sortear)
sortearBotao.grid(row=5, column=1, sticky=W, pady=4)

janela.title('Sorteio CD Py')
janela.mainloop()