
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sqrt, pi


def f(n):
    n = exp(-1*(n * n))
    return n


def graph():

    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize = (8, 5))

    ax = fig.add_subplot(111)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.5, 1.5)

    ax.set_title("The Gaussian integral")

    ax.axhline(y=0, color='darkgray')
    ax.axvline(x=0, color='darkgray')

    x = np.arange(-3, 3, 0.01)
    y = f(x)
    ax.plot(x, y, color='red', label = 'f(x) = $\mathregular{e^{−x^{2}}}$')

    a = -3
    b = 3
    n = 50

    h = (b - a) / n
    s = 0

    for i in range(n):
        xi = a + i * h
        xi2 = a + (i + 1) * h
        yi = f(xi)
        yi2 = f(xi2)
        s += h * (yi + yi2) / 2

        x = [xi, xi]
        y = [0, yi]
        ax.plot(x, y, color='green', alpha= 0.5)

        x = [xi, xi2]
        y = [yi, yi2]
        ax.plot(x, y, color='green', alpha= 0.5)

        ax.fill_between(x, 0, y, facecolor='green', alpha=0.2)

    ax.fill_between(x, 0, y, facecolor='green', alpha=0.2, label = f'Area = {s};')
    ax.plot([], [], ' ', label = f'Interval - [-3, 3], divided in {n} trapezoids')
    ax.plot([], [], ' ', label=f'√π = {sqrt(pi)}')

    ax.legend(framealpha=1, frameon=True, loc="upper center", ncol=2)

    plt.show()

graph()