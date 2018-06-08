from tkinter import *
from myRepo import sort

def sortear():
   membros = [membro1.get(), membro2.get(), membro3.get(), membro4.get(), membro5.get(), membro6.get()]
   sort(membros)

master = Tk()
Label(master, text="Membro 1: ").grid(row=0)
Label(master, text="Membro 2: ").grid(row=1)
Label(master, text="Membro 3: ").grid(row=2)
Label(master, text="Membro 4: ").grid(row=3)
Label(master, text="Membro 5: ").grid(row=4)
Label(master, text="Membro 6: ").grid(row=5)

membro1 = Entry(master)
membro2 = Entry(master)
membro3 = Entry(master)
membro4 = Entry(master)
membro5 = Entry(master)
membro6 = Entry(master)

membro1.grid(row=0, column=1)
membro2.grid(row=1, column=1)
membro3.grid(row=2, column=1)
membro4.grid(row=3, column=1)
membro5.grid(row=4, column=1)
membro6.grid(row=5, column=1)

Button(master, text='Sair', command=master.quit).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Fazer sorteio', command=sortear).grid(row=6, column=1, sticky=W, pady=4)

mainloop()