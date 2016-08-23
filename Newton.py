from matplotlib import *
from Funcoes import *
import time


def newton(ai):
    #   Trata divisão por 0
    if fd(ai) == 0:
        return
    time.sleep(0.2)

    p = ai - (f(ai) / fd(ai))

    print(p, ai, f(ai), fd(ai))
    
    #   Teste de parada
    if (mod(p - ai) < dx) or (mod(p - ai) / mod(p) < dx) or (mod(f(p)) < dx):
        print("Raiz:", p)
        return

    #   Se não para, chama a recursão
    else:
        newton(p)

newton(1.5)
