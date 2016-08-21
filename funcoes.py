from Constantes import *

#   Eixos
ex = [-MAXex, MAXex]
ey = [-MAXex, MAXex]


#   Função a ser desenhada
def funcao(x):
    return sin(x)

#   Gera o intervalo com np pontos de intervalo[0] até intervalo[1]
def getIntervalo(np, intervalo):
    dx = (intervalo[1] - intervalo[0])/np
    x = []
    aux = intervalo[0]
    for i in range(np+1):
        x.append(round(aux, 5))
        aux += dx
    return x
