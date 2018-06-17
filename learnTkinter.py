from tkinter import *

from functools import partial # Importa a funcao 'partial', que reescreve uma funcao
# E importa uma lista de parametros

# Pilares do tkinter:

# Gerenciadores de Layout, Widgets e Eventos
# Um gerenciador de layout define a organização dos widgets dentro de um container

# Os 3 gerenciadores de layout: place, pack e grid
# place - usa coordenadas x e y (a origem fica no canto superior esquerdo do monitor)
# pack - empacota os widgets na horizontal ou vertical
# grid - os widgets são inseridos num sistema de células de uma tabela

def onClick(botao):
    rotulo['text']= botao['text']

janela = Tk() # Instanciando a classe Tk() do pacote tk no objeto 'janela'

botao1 = Button(janela, width=20, text='Botao 1') # Instancie a classe Button no objeto botao
botao1['command'] = partial(onClick, botao1)# Ao utilizar o comando onClick sem os parenteses no final, garantimos que ele nao sera executado antes do clique
botao1.place(x=100, y=100)

botao2 = Button(janela, width=20, text='Botao 2')
botao2['command'] = partial(onClick, botao2)
botao2.place(x=100, y=130)

# Uso: Label(parent, text='string')
rotulo = Label(janela, text='Nenhuma acao realizada') # Instanciando a classe Label no objeto 'rotulo'
rotulo.place(x=100, y=160) # Estabelecendo o gerenciador de layout que deve conter o rotulo


janela.title("Janela principal") # Título da janela
# janela['background'] = 'white' # Toda janela é também um dicionário
janela.geometry('300x300+200+200') #'L' x 'H' + 'X' + 'Y'

janela.mainloop() # Interrompe a execução do script enquanto a janela principal estiver sendo exibida