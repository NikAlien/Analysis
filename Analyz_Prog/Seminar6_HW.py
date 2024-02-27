
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    n = n ** 3
    return n


def f1(n):
    n = 3 * (n ** 2)
    return n


def fh(x, h):
    return (f(x + h) - f(x)) / h


def fh2(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def oh(x, h):
    return abs(f1(x) - ((f(x + h) - f(x)) / h))


def oh2(x, h):
    return abs(f1(x) - ((f(x + h) - f(x - h)) / (2 * h)))


def graph():

    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize = (12, 4))

    ax = fig.add_subplot(131)
    bx = fig.add_subplot(132)
    cx = fig.add_subplot(133)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 5)

    ax.set_title("Function and its derivative")
    bx.set_title("First order approximation")
    cx.set_title("Second order approximation")

    ax.axhline(y=0, color='darkgray')
    ax.axvline(x=0, color='darkgray')

    bx.axhline(y=0, color='darkgray')
    bx.axvline(x=0, color='darkgray')

    cx.axhline(y=0, color='darkgray')
    cx.axvline(x=0, color='darkgray')

    x = np.arange(-4, 4, 0.01)
    y = f(x)
    ax.plot(x, y, color='red', label = 'f(x) = x³')

    x = np.arange(-4, 4, 0.01)
    y = f1(x)
    ax.plot(x, y, color='green', label="f'(x) = 3x²")

    x = 1
    h = np.arange(1.25, 0.001, -0.001)

    y = fh(x, h)
    bx.plot(h, y, color='red', label="f'(X0)")

    y = oh(x, h)
    bx.plot(h, y, color='green', label="O(h)")
    bx.plot(h, h, color='orange', label="h -> [0.001, 1.25]")

    y = fh2(x, h)
    cx.plot(h, y, color='red', label="f'(X0)")

    y = oh2(x, h)
    cx.plot(h, y, color='green', label="O(h²)")
    cx.plot(h, h, color='orange', label="h -> [0.001, 1.25]")

    ax.plot(1, 3, 'o', color='chocolate', label='X0 = 1')
    bx.plot(0, 3, 'o', color='chocolate', label="f'(X0) = 3")
    cx.plot(0, 3, 'o', color='chocolate', label="f'(X0) = 3")

    ax.legend(framealpha=1, frameon=True, loc="upper center", ncol=2)
    bx.legend(framealpha=1, frameon=True, loc="upper center", ncol=2)
    cx.legend(framealpha=1, frameon=True, loc="upper center", ncol=2)

    plt.show()

graph()
