from Config import *

#   Gera o intervalo com np pontos de intervalo[0] até intervalo[1]
def getIntervalo(np, intervalo):
    dx = (intervalo[1] - intervalo[0])/np
    x = []
    aux = intervalo[0]
    for i in range(np+1):
        x.append(round(aux, p))
        aux += dx
    return x

def mod(num):
    if num < 0: return -num
    else:   return num

def testaIntervalo(a, b, nit):
    if not f(a) * f(b) < 0:
        if f(a) == 0:
            print("Raiz:", a, "\nIteracoes:", nit)
        elif f(b) == 0:
            print("Raiz:", b, "\nIteracoes:", nit)
        else:
            print("intervalo invalido")
        quit()
