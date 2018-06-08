import tkinter as tk
from random import shuffle

class Sorteio(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.membros = list()

        for i in range(6):
            self.memberLabel = tk.Label(self, text="Membro " + str(i + 1) + ": ")
            self.memberLabel.grid(row=i)
            self.membros.append(tk.Entry(self))
            self.membros[i].grid(row=i, column=1)

        self.quitButton = tk.Button(self, text='Sair', command=self.quit)
        self.quitButton.grid(row=6, column=0, sticky=tk.W, pady=4)

        self.sortButton = tk.Button(self, text='Fazer sorteio', command=self.sort(self.membros))
        self.sortButton.grid(row=6, column=1, sticky=tk.W, pady=4)

    def sort(self, membros):
        self.members = [element.get() for element in membros]
        self.results = tk.Text(self, height=26, width=30)
        self.results.grid()

        self.results.insert(tk.END, "Tempo total da rodada: %d min\n" % (len(self.members) * 10))
        shuffle(self.members)

        for i in range(1, len(self.members)):
            self.results.insert(tk.END, "\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" % (i, self.members[i - 1], self.members[i]))
            if (i == len(self.members) - 1):
                self.results.insert(tk.END, "\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" % (len(self.members), self.members[len(self.members) - 1], self.members[0]))

app = Sorteio()
app.master.title("Roleta Russa do CD Py")
app.mainloop()