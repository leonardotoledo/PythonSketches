# CALCULO DE BLOCO QUADRADO DE FUNDACAO

# Esta funcao calcula as dimensoes de um bloco de fundacao quadrado (B=L).
from tkinter import *
from math import *

def calcBloco():
    fck = float(number1.get())
    P = float(number2.get())
    TT = float(number3.get())
    b = float(number4.get())
    l = float(number5.get())

    # fck = fck do concreto (MPa).
    # P = Carga do pilar, após aplicados os coeficientes de majoracao (kgf).
    # TT = Valor da taxa do terreno (kgf/cm²).
    # b = lado menor do pilar (cm).
    # l = lado maior do pilar (cm).

    # A funcao retornara as dimensoes do bloco, em centimetros, na seguinte ordem: B, H.

    B = sqrt(1.05*P/TT) # Calculando o valor da base do bloco.
    fct = 0.084*pow(fck,2/3)
    fct = 10*fct # Convertendo de MPa para kgf/cm²
    if fct>8:
        fct=8

    Beta = 0.01
    aux = TT/fct+1
    while (tan(Beta)/Beta < aux):
        Beta = atan(Beta*aux)


    if (B-b) >= (B-l):
        H = tan(Beta)*(B-b)/2 # Calculando a altura do bloco
        z = 1.05*P*(B-b)/4/H # Calculando a tracao transveral de Morsch
    else:
        H = tan(Beta)*(B-l)/2  # Calculando a altura do bloco
        z = 1.05*P*(B-l)/4/H # Calculando a tracao transveral de Morsch

    t = z/H/B;

    if t>8:
        H = z/8/B

    resultado = Label(window, text="Base do Bloco: %.2f\nAltura: %.2f"%(B,H))
    resultado.grid(row=6, column=1)


# resultado = calcBloco(20,50000,5,15,40)
#
# print("Largura da Base: %.2f\nAltura do Bloco: %.2f"%(resultado[0],resultado[1]))

window = Tk()

rotulo1 = Label(window, text='fck do Concreto (MPa): ')
rotulo1.grid(row=0, column=0)

rotulo2 = Label(window, text='Carga do Pilar (kgf): ')
rotulo2.grid(row=1, column=0)

rotulo3 = Label(window, text='Taxa do Terreno (kgf/cm²): ')
rotulo3.grid(row=2, column=0)

rotulo4 = Label(window, text='Lado menor do Pilar (cm): ')
rotulo4.grid(row=3, column=0)

rotulo5 = Label(window, text='Lado maior do Pilar (cm): ')
rotulo5.grid(row=4, column=0)

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

sairBotao = Button(window, text='Sair', command=window.quit).grid(row=5, column=0, sticky=W, pady=4)
contarBotao = Button(window, text='Calcular Bloco', command = calcBloco).grid(row=5, column=1, sticky=W, pady=4)

window.title('Sorteio CD Py')
window.mainloop()