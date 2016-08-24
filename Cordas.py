from Funcoes import *

def cordas(a, b, nit):
    #   Testa se há pelo menos uma raiz no intervalo
    testaIntervalo(a, b, nit)

    x = (a * f(b) - b * f(a)) / (f(b) - f(a))

    #   Teste de parada
    if mod(f(x)) < dx:
        print("Raiz:", x)
        print("Iteracoes:", nit)
        return

    #   Escolha da recursão
    if f(x) * f(b) < 0:
        a = x
    else:
        b = x
    cordas(a, b, nit + 1)

cordas(0, 2, 0)
