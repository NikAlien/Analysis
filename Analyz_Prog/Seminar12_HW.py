
import matplotlib.pyplot as plt
import numpy as np

def f(fx, fy, b):
    return (fx ** 2 + b * (fy ** 2)) / 2

def step(fx, fy, b):
    return (fx ** 2 + (b ** 2) * (fy ** 2)) / (fx ** 2 + (b ** 3) * (fy ** 2))

def next_iteration(fx, fy, fs, b):
    return [(1 - fs) * fx, (1 - b * fs) * fy]

br = [0.5, 0.2, 0.1, 1]
fig = plt.figure(figsize = (20, 20))

ax = fig.add_subplot(221)
bx = fig.add_subplot(222)
cx = fig.add_subplot(223)
dx = fig.add_subplot(224)


ax.set_title("b = 0.5")
bx.set_title("b = 0.2")
cx.set_title("b = 0.1")
dx.set_title("b = 1, in this case the coordinates arrive in one step")

sh = [ax, bx, cx, dx]

for i in range(4):

    if br[i] == 1:
        iterations = 2
    else:
        iterations = 10
    x = np.zeros(iterations + 2)
    y = np.zeros(iterations + 2)

    x[0] = 1
    y[0] = 0.5

    k = 0
    s = step(x[k], y[k], br[i])
    [x[k+1], y[k+1]] = next_iteration(x[k], y[k], s, br[i])

    while k < iterations:
        if br[i] == 1:
            break
        # print(k, x[k], y[k], f(x[k], y[k], br[i]))
        k += 1
        s = step(x[k], y[k], br[i])
        [x[k + 1], y[k + 1]] = next_iteration(x[k], y[k], s, br[i])

    xlist = np.linspace(-1.0, 1.0, 100)
    ylist = np.linspace(-1.0, 1.0, 100)
    xx, yy = np.meshgrid(xlist, ylist)
    zz = f(xx, yy, 1)

    nlevels = 4
    if br[i] == 1:
        nlevels = 1
    levels = np.zeros(nlevels + 2)
    for k in range(nlevels):
        levels[k] = f(x[k], y[k], br[i])
    levels[nlevels], levels[nlevels + 1] = [1,0.5]
    levels = np.sort(levels)

    contours = plt.contour(xx, yy, zz, levels)
    sh[i].clabel(contours, inline=True, fontsize=8)

    sh[i].plot(x[:iterations], y[:iterations], 'r--o')

    sh[i].contour(xx, yy, zz, levels = 5)



plt.show()