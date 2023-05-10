import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from textwrap import wrap

with open('settings.txt') as f:
    s = f.read().split('\n')
    set = [float(i) for i in s]

data_u = np.loadtxt("data.txt", dtype = float)
data_t = np.array([i / set[0] for i in range(data_u.size)])

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)

#мин и макс значения на осях
ax.axis([data_t.min(), data_t.max()+5, data_u.min(), data_u.max()+0.3])

#интервалы делений на осях 
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#подписи осей и графика
name = "Процесс зарядки и разрядки конденсатора в rc-цепи"
ax.set_title("\n".join(wrap(name, 60)), loc = 'center', fontsize = 30)
ax.set_ylabel("Напряжение, В", fontsize = 15)
ax.set_xlabel("Время, с", fontsize = 15)

#сетка
ax.grid(which = 'major', color = 'k')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'gray', linestyle = ':')

#текст
text1 = "Время зарядки: 22.3c"
text2 = "Время разрядки: 31.3c"
ax.text(40, 2.05, text2, fontsize = 15, color = 'blue')
ax.text(40, 2.15, text1, fontsize = 15, color = 'blue')

#линия графика
ax.plot(data_t, data_u, c = 'green', linewidth = 2, label='U(t)')

#маркеры
ax.scatter(data_t[0:data_u.size:10], data_u[0:data_u.size:10], marker = 's', c = 'red', s = 15)

#легенда графика
ax.legend(shadow = 0, loc = 'upper right', fontsize = 20)

fig.savefig("graph.png")
fig.savefig("graph.svg")
print("ok")