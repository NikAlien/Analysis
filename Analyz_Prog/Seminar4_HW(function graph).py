
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    n = ((-1) ** (n + 1)) / n
    return n

def graph():
    ln = np.log(2)

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    fig.suptitle("Homework - Carp Nicoleta")
    ax.set_title("Sum of the series")
    ax.set_ylim(0.2, 1)
    plt.axhline(ln, color = 'darkorange', label = ln)

    e = 0.001
    sum_new = f(1)
    sum2 = f(1)
    i = 1
    k = 0
    len = 1
    counter = 0
    points = []
    ax.hlines(sum_new, i, i + 0.9999999, color='navy', linewidth=2, label='Sum of arranged nr')
    ax.hlines(sum2, len, len + 0.9999999, color='maroon', linewidth=2)

    while np.abs(ln - sum_new) > e:
        i += 1
        n = f(i)
        sum_new += n
        if i % 2 == 0:
            sum2 += n
            counter += 1
            len += 1
            ax.hlines(sum2, len, len + 0.9999999, color='maroon', linewidth=2)
        else:
            points.append(n)
        ax.hlines(sum_new, i, i + 0.9999999, color = 'navy', linewidth = 2)

        if counter == 2:
            counter = 0
            sum2 += points[k]
            k += 1
            len += 1

    plt.axhline(sum2, color = 'g', label = sum2)
    ax.hlines(sum2, len, len + 0.9999999, color='maroon', linewidth=2, label='Sum of rearranged nr')
    plt.legend(framealpha=1, frameon=True, loc = "upper center", ncol = 2)
    plt.show()

graph()
