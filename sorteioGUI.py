import tkinter as tk
from random import shuffle

class InputView(tk.Frame):

    def sort(self, members):

        file = open("resultado.txt", "w")

        file.write("Tempo total da rodada: %d min\n" % (len(members) * 10))

        shuffle(members)

        for i in range(1, len(members)):
            file.write("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" % (i, members[i - 1], members[i]))
            if (i == len(members) - 1):
                file.write("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" % (
                len(members), members[len(members) - 1], members[0]))

        file.close()

    def sortear(self):
        membros = []
        for i in range(len(self.members)):
            membros.append(self.members[i].get())
        self.sort(membros)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.members = list()

        for i in range(5):
            self.memberLabel = tk.Label(self, text="Membro " + str(i + 1) + ": ")
            self.memberLabel.grid(row=i, column=0)
            self.members.append(tk.Entry(self))
            self.members[i].grid(row=i, column=1)

        self.people = [person.get() for person in self.members]

        self.quitButton = tk.Button(self, text='Sair', command=self.quit)
        self.quitButton.grid(row=len(self.members)+1, column=0, sticky=tk.W, pady=4)

        self.sortButton = tk.Button(self, text='Fazer sorteio', command=self.sortear)
        self.sortButton.grid(row=len(self.members)+1, column=1, sticky=tk.W, pady=4)

app = InputView()
app.master.title("Roleta Russa do CD Py")
app.mainloop()