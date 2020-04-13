import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon


def f(x):
    return 3 * (x ** 3) + 3 * x + 1


# Tinh
i, e = integrate.quad(lambda k: f(k), 0, 3)
print(i)

fig, ax = plt.subplots()

x = np.linspace(0, 5)
y = f(x)

# draw
ax.plot(x, y, 'red')

a, b = 0, 3

ix = np.linspace(a, b)
iy = f(ix)

# list luu lai cac diem
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor="orange")
ax.add_patch(poly)
plt.show()
