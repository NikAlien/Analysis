
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    n = n * n
    return n

def f1(n):
    n = 2 * n
    return n

def fb(n):
    n = n ** 4 - n ** 3 - 5 * n * n
    return n

def fb1(n):
    n = 4 * (n ** 3) - 3 * (n ** 2) - 10 * n
    return n

def graph():

    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize = (15, 7))
    ax = fig.add_subplot(121)
    bx = fig.add_subplot(122)
    fig.suptitle("Homework Seminar 5 - Carp Nicoleta")
    ax.set_ylim(0, 1250)
    ax.set_xlim(-40, 40)
    ax.set_title("Convex and differentiable function")

    bx.set_ylim(-15, 10)
    bx.set_xlim(-5, 5)
    bx.set_title("Nonconvex and differentiable function")

    x = np.arange(-25, 25, 0.01)
    y = f(x)
    ax.plot(x, y, color='blue', label = 'f(x) = x²')

    eps = 0.001
    const = 0.4
    x = [-25]
    y = [f(x[0])]
    i = 0

    while abs(y[i]) > eps:
        x.append(x[i] - const * f1(x[i]))
        y.append(f(x[i + 1]))
        i += 1

    ax.plot(x, y, 'o--', color='red', label = 'n = 0.4')

    const = 0.9
    x = [-25]
    y = [f(x[0])]
    i = 0

    while abs(y[i]) > eps:
        x.append(x[i] - const * f1(x[i]))
        y.append(f(x[i + 1]))
        i += 1

    ax.plot(x, y, 'o--', color='green', label = 'n = 0.9')

    const = 1.2
    x = [-25]
    y = [f(x[0])]

    for i in range(10):
        x.append(x[i] - const * f1(x[i]))
        y.append(f(x[i + 1]))

    ax.plot(x, y, 'o--', color='orange', label = 'n = 1.2')
    ax.legend(framealpha=1, frameon=True, loc = "upper center", ncol = 2)

    x = np.arange(-5, 5, 0.01)
    y = fb(x)

    bx.plot(x, y, color='blue', label='f(x) = x^4 - x^3 - 5(x^2)')

    const = 0.045
    x = [-2]
    y = [fb(x[0])]

    for i in range(50):
        x.append(x[i] - const * fb1(x[i]))
        y.append(fb(x[i + 1]))

    bx.plot(x, y, 'o--', color='red', label='n = 0.045')
    bx.legend(framealpha=1, frameon=True, loc="upper center", ncol=2)
    ax.plot(0, 0, 'o', color = 'navy')
    bx.plot(-1.3, -3.4, 'o', color='navy')
    plt.show()

graph()
