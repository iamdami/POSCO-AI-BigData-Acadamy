import numpy as np

x = np.ones((5, 5))
print("oringnal of 1: \n", x)

x[1:-1, 1:-1] = 0
print("1 padded: \n", x)

z = np.zeros((5, 5))
print("oringnal of 2: \n", z)
z[1:-1, 1:-1] = 1
print("1 padded: \n", z)