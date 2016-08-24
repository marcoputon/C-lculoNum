from math import *

#   Constantes
MAXex = 10              #   Tamanho do eixo X
MAXey = 3               #   Tamanho do eixo Y
npontos = 90000         #   Quantidades de pontos a ser desenhado
intervalo = [-1, 2]   	#   Intervalo a ser desenhado
p = 7                   #   Número de casas (Para a precisão)
dx = 10**-p             #   Precisão do calculo de raiz

#   Eixos
ex = [-MAXex, MAXex]
ey = [-MAXex, MAXex]

#   Função
def f(x):
    return x*(e**x)-2

#   Derivada da função f(x)
def fd(x):
    return 1/(3*(2**(2/3)))
