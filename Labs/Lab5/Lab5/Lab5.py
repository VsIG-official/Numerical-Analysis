
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

# Number of unknowns
n = 3

# Making numpy array of n & n x n size and initializing
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))

def MySinFun(x: int, alpha=3) -> float:
    y_value = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return y_value

def MyNonSinFun(x: int, alpha=3) -> float:
    y_value = x ** (1. / 3.)
    return y_value

#x = [3, 5, 7, 9, 11]
#y = [MySinFun(x[0]), MySinFun(x[1]), MySinFun(x[2]), MySinFun(x[3]), MySinFun(x[4])]

x = [1, 2, 3]
y = [MyNonSinFun(x[0]), MyNonSinFun(x[1]), MyNonSinFun(x[2])]

# Implementing Lagrange Interpolation
def Lagrange(xp, x, y) -> [list, list]:
    # Set interpolated value initially to zero
    yp = 0
    for i in range(n):

        p = 1

        for j in range(n):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])

        yp = yp + p * y[i]

        print("x =", x[i], " y =", y[i])
    return xp, yp

for i in range(n):
    tempXP , tempYP = Lagrange(x[i], x, y)
    print('Interpolated value at %.3f is %.3f.' % (tempXP, tempYP))
