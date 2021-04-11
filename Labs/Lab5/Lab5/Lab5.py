
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5

# region Identity

def Identity(N):
    matrixForIdentity = [[0 for x in range(N)] for y in range(N)]
    for i in range(0, N):
        matrixForIdentity[i][i] = 1
    return matrixForIdentity

# endregion Identity

# region Prints

# print matrix
def PrintMatrixAsNp(matrixName,matrix):
    print("\n", matrixName,"=")
    npMatrix = np.array(matrix)
    print(npMatrix.round(rounding))

# print matrix
def PrintVectorAsNp(vectorName, vector):
    print("\n", vectorName,"=")
    npMatrix = np.array(vector)
    print(npMatrix.round(rounding))

# print additional parametrs
def PrintParametrs():
    print("\nN =", N)

# endregion Prints

def MySinFun(x: int, alpha=3) -> float:
    y_value = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return y_value

def MyNonSinFun(x: int) -> float:
    y_value = x ** (1. / 3.)
    return y_value

#x = [3, 5, 7, 9, 11]
#y = [MySinFun(x[0]), MySinFun(x[1]), MySinFun(x[2]), MySinFun(x[3]), MySinFun(x[4])]

X_array = [1, 2, 3]
Y_array = [MyNonSinFun(X_array[0]), MyNonSinFun(X_array[1]), MyNonSinFun(X_array[2])]

# Implementing Lagrange Interpolation
def Lagrange(x, y):
    PrintVectorAsNp("X", X_array)
    PrintVectorAsNp("Y", Y_array)

Lagrange(X_array, Y_array)
