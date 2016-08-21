import matplotlib
from matplotlib import *
import matplotlib.pyplot as plt
from math import sin, cos, pi
from funcoes import *

#   Desenha os eixos x e y:
plt.plot(ex, [0, 0], color="black")
plt.plot([0, 0], ey, color="black")


x = getIntervalo(npontos, intervalo)
y = []
for i in x:
    y.append(funcao(i))


#plt.figure(figsize=(10, 5))
plt.title('Teste')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

ax = plt.gca()
y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
ax.yaxis.set_major_formatter(y_formatter)



plt.plot(x, y, color="red", label="y=2x")
plt.legend()

plt.show()
