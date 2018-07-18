from tkinter import *
from math import *


def calcSapata():
    c = float(number1.get())
    fck = float(number2.get())
    fyk = float(number3.get())
    P = float(number4.get())
    TT = float(number5.get())
    b = float(number6.get())
    l = float(number7.get())
    r = float(number8.get())

    # c = cobrimento da armadura (cm).
    # fck = fck do concreto (MPa).
    # fyk = Resistencia ao escoamento do Aco (MPa).
    # P = Carga do pilar, após aplicados os coeficientes de majoracao (kgf).
    # TT = Valor da taxa do terreno (kgf/cm²).
    # b = lado menor do pilar (cm).
    # l = lado maior do pilar (cm).
    # r = razão entre L e B (L/B).

    B = sqrt(P/TT/r)  # Calculando o valor do lado B da base da sapata.
    L = r*B  # Calculando o valor do lado L da base da sapata.
    fck = 10*fck  # Convertendo de MPa para kgf/cm²
    fyk = 10 * fyk  # Convertendo de MPa para kgf/cm²

    # CALCULO DA ALTURA DA SAPATA

    sigmac = 0.85*fck/1.96

    h1 = (L-l)/3
    h2 = (B-b)/3
    h3 = 1.44*sqrt(P/sigmac)+5

    comp = [h1, h2, h3]
    comp.sort()

    h = comp[2] # Determinacao da maior altura

    # ARREDONDAMENTO DAS DIMENSOES PARA MULTIPLOS DE 5

    modulusB = int(B/5)
    modulusL = int(L/5)
    modulosH = int(h/5)

    B = 5*(modulusB + 1)
    L = 5*(modulusL + 1)
    h = 5*(modulosH + 1)

    # CALCULO DAS ARMADURAS

    dlinha = c
    d = h - dlinha

    Fx = P*(L-l)/(8*d)
    Fy = P*(B-b)/(8*d)

    fyd = fyk/1.15

    Asx = 1.4*Fx/fyd
    Asy = 1.4*Fy/fyd

    Barras = {'6.3': 0.312, '8.0': 0.503, '10.0': 0.785, '12.5': 1.227, '16.0': 2.011, '20.0': 3.142} # Fonte: Pg.10 NBR 7480:2008

    Areas = list(Barras.values())
    Bitolas = list(Barras.keys())

    # DETALHAMENTO DA ARMADURA EM X

    sx = 0
    i = 0 # Loop index
    comprimentoX = L-2*c+2*10

    while (sx<8 or sx>33):
        nx = int(Asx/Areas[i])+1 # Numero de barras
        sx = (B - 2*c)/(nx-1)
        detalheX = '%d bitolas de %s c/ %.1f c. %.1f'%(nx,Bitolas[i],sx,comprimentoX)
        i = i+1

    # DETALHAMENTO DA ARMADURA EM Y

    sy = 0
    i = 0 # Loop index
    comprimentoY = B - 2 * c + 2 * 10

    while (sy<8 or sy>33):
        ny = int(Asy/Areas[i])+1 # Numero de barras
        sy = (L - 2*c)/(ny-1)
        detalheY = '%d bitolas de %s c/ %.1f c. %.1f'%(ny,Bitolas[i],sy,comprimentoY)
        i = i+1

    resultado = Label(window, text="RESULTADOS: ")
    resultado.grid(row=9, column=0)

    resultado_base = Label(window, text="Base: %.2f cm"%(B))
    resultado_base.grid(row=9, column=1)

    resultado_largura = Label(window, text="Largura: %.2f cm" %(L))
    resultado_largura.grid(row=10, column=1)

    resultado_altura = Label(window, text="Altura: %.2f cm" %(h))
    resultado_altura.grid(row=11, column=1)

    resultado_detalheX = Label(window, text=detalheX)
    resultado_detalheX.grid(row=12, column=1)

    resultado_detalheY = Label(window, text=detalheY)
    resultado_detalheY.grid(row=13, column=1)

window = Tk()

rotulo1 = Label(window, text='Cobrimento da Armadura (cm): ')
rotulo1.grid(row=0, column=0)

rotulo2 = Label(window, text='fck do Concreto (MPa): ')
rotulo2.grid(row=1, column=0)

rotulo3 = Label(window, text='fck do Aco (MPa): ')
rotulo3.grid(row=2, column=0)

rotulo4 = Label(window, text='Carga do Pilar (kgf): ')
rotulo4.grid(row=3, column=0)

rotulo5 = Label(window, text='Taxa do Terreno (kgf/cm²): ')
rotulo5.grid(row=4, column=0)

rotulo6 = Label(window, text='Lado menor do Pilar (cm): ')
rotulo6.grid(row=5, column=0)

rotulo7 = Label(window, text='Lado maior do Pilar (cm): ')
rotulo7.grid(row=6, column=0)

rotulo8 = Label(window, text='Razão L/B: ')
rotulo8.grid(row=7, column=0)

number1 = Entry(window)
number1.grid(row=0, column=1)

number2 = Entry(window)
number2.grid(row=1, column=1)

number3 = Entry(window)
number3.grid(row=2, column=1)

number4 = Entry(window)
number4.grid(row=3, column=1)

number5 = Entry(window)
number5.grid(row=4, column=1)

number6 = Entry(window)
number6.grid(row=5, column=1)

number7 = Entry(window)
number7.grid(row=6, column=1)

number8 = Entry(window)
number8.grid(row=7, column=1)

sairBotao = Button(window, text='Sair', command=window.quit).grid(row=8, column=0, sticky=W, pady=4)
contarBotao = Button(window, text='Calcular Sapata', command = calcSapata).grid(row=8, column=1, sticky=W, pady=4)

window.title('Sapata de Fundacao')
window.mainloop()
