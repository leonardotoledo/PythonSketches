from tkinter import *
from myRepo import sort

def sortear():
   membros = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()]
   sort(membros)

master = Tk()
Label(master, text="Membro 1: ").grid(row=0)
Label(master, text="Membro 2: ").grid(row=1)
Label(master, text="Membro 3: ").grid(row=2)
Label(master, text="Membro 4: ").grid(row=3)
Label(master, text="Membro 5: ").grid(row=4)
Label(master, text="Membro 6: ").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

Button(master, text='Sair', command=master.quit).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Fazer sorteio', command=sortear).grid(row=6, column=1, sticky=W, pady=4)

mainloop( )