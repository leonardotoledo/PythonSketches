# CALCULO DE BLOCO QUADRADO DE FUNDACAO

# Esta funcao calcula as dimensoes de um bloco de fundacao quadrado (B=L).
from math import *

def calcBloco(fck,P,TT,b,l)
    # fck = fck do concreto (MPa).
    # P = Carga do pilar, após aplicados os coeficientes de majoracao (kgf).
    # TT = Valor da taxa do terreno (kgf/cm²).
    # b = lado menor do pilar (cm).
    # l = lado maior do pilar (cm).

    # A funcao retornara as dimensoes do bloco, em centimetros, na seguinte ordem: B, H.

    fck = 10*fck # Convertendo de MPa para kgf/cm²
    B = sqrt(1.05*P/TT) # Calculando o valor da base do bloco.
    L = B # Calculando o valor da largura do bloco.
    fct = 0.084*pow(fck,2/3)
    if fct>8:
        fct=8





    return B,L


B = calcBloco(20,50000,5,15,40)
print(B)