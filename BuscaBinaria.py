from Funcoes import *

def bisseccao(a, b, nit):
    #   Testa se há pelo menos uma raiz no intervalo
    testaIntervalo(a, b, nit)

    c = (a + b) / 2

    #   Teste de parada
    if (f(c) >= 0 and f(c) <= dx) or (f(c) < 0 and f(c) >= -dx):
        print("Raiz:", c)
        print("Iteracoes:", nit)
        return

    #   Chamada da recursiva para o lado certo
    else:
        if f(c) * f(a) < 0:
            bisseccao(a, c, nit + 1)
        elif f(c) * f(b) < 0:
            bisseccao(c, b, nit + 1)

bisseccao(1, 8, 0)
