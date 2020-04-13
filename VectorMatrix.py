import numpy as np
import matplotlib.pyplot as plt
from sympy import true

v = np.array([2, 1])
s = np.array([-3, 2])
z = v + s
origin = np.array([0, 0])
print(v)

ax = plt.axes()
ax.arrow(*origin, *v, head_width=0.2, head_length=0.2, length_includes_head=true, fc='red', ec='red')
ax.arrow(*origin, *s, head_width=0.2, head_length=0.2, length_includes_head=true, fc='green', ec='green')
ax.arrow(*origin, *z, head_width=0.2, head_length=0.2, length_includes_head=true, fc='yellow', ec='yellow')
plt.xticks(np.arange(-5, 5, 1))
plt.yticks(np.arange(-5, 5, 1))
plt.axis('square')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
# plt.show()

print(np.dot(v, s))  # tich vo huong

vector1 = np.array([1, 2, 3])
vector2 = np.array([[4, 5, 6]])
print(np.cross(vector1, vector2))  # tich co huong

# ma tran
A = np.matrix([[1, 2, 3],
               [4, 5, 6]])
B = np.matrix([[2, 2, 2],
               [2, 2, 2]])
print(A)
print(B)
# chuyen vi
print(A.T)
# tich voi 1 so
print(2 * A)
# tich vo huong
print(np.dot(A, B.T))
print(A @ B.T)
# ma tran nghich dao
V = np.array([[1, 2],
             [3, 4]])
print(V)
V_inv = np.linalg.inv(V)
print(V_inv)
print(V @ V_inv)
