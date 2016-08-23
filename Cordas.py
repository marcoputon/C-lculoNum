from Funcoes import *

def cordas(a, b):
    #   Testa se há pelo menos uma raiz no intervalo
    testaIntervalo(a, b)

    x = (a * f(b) - b * f(a)) / (f(b) - f(a))

    #   Teste de parada
    if mod(f(x)) < dx:
        print(x)
        return

    #   Escolha da recursão
    if f(x) * f(b) < 0:
        a = x
    else:
        b = x
    cordas(a, b)

cordas(3, 5)
