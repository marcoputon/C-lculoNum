from matplotlib import *
from Funcoes import *
import time


def newton(ai, nit):
    #   Trata divisão por 0
    if fd(ai) == 0:
        return
	
    p = ai - (f(ai) / fd(ai))
    
    #   Teste de parada
    if (mod(p - ai) < dx) or (mod(p - ai) / mod(p) < dx) or (mod(f(p)) < dx):
        print("Raiz:", p)
        print("Iteracoes:", nit)
        return

    #   Se não para, chama a recursão
    else:
        newton(p, nit + 1)

newton(1.5, 0)
