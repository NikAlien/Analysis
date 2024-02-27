import numpy as np
import matplotlib.pyplot as plt

def graph():

    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize = (8, 8))

    ax = fig.add_subplot(221)
    bx = fig.add_subplot(222)
    cx = fig.add_subplot(223)
    dx = fig.add_subplot(224)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    bx.set_xlim(-1.5, 1.5)
    bx.set_ylim(-1.5, 1.5)

    cx.set_xlim(-1.5, 1.5)
    cx.set_ylim(-1.5, 1.5)

    dx.set_xlim(-1.5, 1.5)
    dx.set_ylim(-1.5, 1.5)

    ax.set_title("The unit ball for p = 1.25")
    bx.set_title("The unit ball for p = 1.5")
    cx.set_title("The unit ball for p = 3")
    dx.set_title("The unit ball for p = 8")

    x = np.arange(-1, 1, 0.01)
    y = np.arange(-1, 1, 0.01)
    l = len(x)

    fin_x = []
    fin_y = []

    for i in range(l):
        for j in range(l):
            if (abs(x[i]) ** 1.25 + abs(y[j]) ** 1.25) ** 0.8 <= 1:
                fin_x.append(x[i])
                fin_y.append(y[j])

    ax.plot(fin_x, fin_y, color='red')

    fin_x = []
    fin_y = []

    for i in range(l):
        for j in range(l):
            if (abs(x[i]) ** 1.5 + abs(y[j]) ** 1.5) ** (2 / 3) <= 1:
                fin_x.append(x[i])
                fin_y.append(y[j])

    bx.plot(fin_x, fin_y, color='red')

    fin_x = []
    fin_y = []

    for i in range(l):
        for j in range(l):
            if (abs(x[i]) ** 3 + abs(y[j]) ** 3) ** (1 / 3) <= 1:
                fin_x.append(x[i])
                fin_y.append(y[j])

    cx.plot(fin_x, fin_y, color='red')

    fin_x = []
    fin_y = []

    for i in range(l):
        for j in range(l):
            if (abs(x[i]) ** 8 + abs(y[j]) ** 8) ** (1 / 8) <= 1:
                fin_x.append(x[i])
                fin_y.append(y[j])

    dx.plot(fin_x, fin_y, color='red')

    plt.show()

graph()