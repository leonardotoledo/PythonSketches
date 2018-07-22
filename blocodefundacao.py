from tkinter import *
from math import pow, sqrt, tan, atan


def ajuda():
    ajuda = Tk()
    ajuda.title('Ajuda')

    texto = Label(ajuda,
                  text='Créditos:\n\n\nLeonardo Tolêdo Ferreira\n\nSite: leonardotoledo.org\n\nE-mail: contato@leonardotoledo.org\n\n\nReferências:\n\nABNT NBR 6118:2014\n\nABNT NBR 6122:2010\n\nABNT NBR 7480:2007\n\nNotas de aula de Fundações 2\nProfª. Drª Juliane Andréia Figueiredo Marques\n\n\nNão me responsabilizo pelo uso\ndeste programa por terceiros.\n')
    texto.grid(row=0, column=0)


def calcBloco():
    fck = float(number1.get())
    P = float(number2.get())
    TT = float(number3.get())
    b = float(number4.get())
    l = float(number5.get())
    r = float(number6.get())

    # fck = fck do concreto (MPa).
    # P = Carga do pilar, após aplicados os coeficientes de majoracao (tf).
    # TT = Valor da taxa do terreno (kgf/cm²).
    # b = lado menor do pilar (cm).
    # l = lado maior do pilar (cm).
    # r = razao L/B

    # A funcao retornara as dimensoes do bloco, em centimetros, na seguinte ordem: B, H.

    P = 1000 * P  # Convertendo para kgf

    B = sqrt(1.05 * P / TT / r)  # Calculando o valor da base do bloco.

    # Arredondamento da base:
    modulusB = int(B / 5)
    B = 5 * (modulusB + 1)

    L = r * B

    if fck == 20:
        fct = 0.4*1.55
    elif fck == 25:
        fct = 0.4*1.80
    else:
        fct = 0.8

    Beta = 0.01
    righthandside = ((TT / 10) / fct) + 1
    lefthandside = tan(Beta)/Beta
    i = 0
    while lefthandside <= righthandside:
        Beta = atan(Beta*righthandside)
        lefthandside = tan(Beta) / Beta
        i+=1
        if i==100:
            break

    if (B - b) > (L - l):
        H = tan(Beta) * (B - b) / 2  # Calculando a altura do bloco
        z = 1.05 * P * (B - b) / 4 / H  # Calculando a tracao transveral de Morsch
    else:
        H = tan(Beta) * (L - l) / 2  # Calculando a altura do bloco
        z = 1.05 * P * (L - l) / 4 / H  # Calculando a tracao transveral de Morsch

    modulosH = int(H / 5)
    H = 5 * (modulosH + 1)

    result = Tk()
    result.title('Resultado')

    resultado = Label(result, text='RESULTADOS: ')
    resultado.grid(row=0, column=0)

    resultado_base = Label(result, text='Base: %.2f cm' % (B))
    resultado_base.grid(row=1, column=0)

    resultado_largura = Label(result, text='Largura: %.2f cm' % (L))
    resultado_largura.grid(row=2, column=0)

    resultado_altura = Label(result, text='Altura: %.2f cm' % (H))
    resultado_altura.grid(row=3, column=0)


window = Tk()

rotulo1 = Label(window, text='fck do Concreto (MPa): ')
rotulo1.grid(row=0, column=0)

rotulo2 = Label(window, text='Carga do Pilar (tf): ')
rotulo2.grid(row=1, column=0)

rotulo3 = Label(window, text='Taxa do Terreno (kgf/cm²): ')
rotulo3.grid(row=2, column=0)

rotulo4 = Label(window, text='Lado do Pilar // a B (cm): ')
rotulo4.grid(row=3, column=0)

rotulo5 = Label(window, text='Lado do Pilar // a L (cm): ')
rotulo5.grid(row=4, column=0)

rotulo6 = Label(window, text='Razão L/B: ')
rotulo6.grid(row=5, column=0)

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

ajudaBotao = Button(window, text='Ajuda', command=ajuda).grid(row=6, column=0, sticky=W, pady=4)
contarBotao = Button(window, text='Calcular Bloco', command=calcBloco).grid(row=6, column=1, sticky=W, pady=4)

window.title('Bloco de Fundacao')
window.mainloop()
