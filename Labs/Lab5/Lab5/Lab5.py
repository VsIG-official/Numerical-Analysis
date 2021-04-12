
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5

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

X_array = [1, 3, 5, 7, 9]
Y_array = [MySinFun(X_array[0]), MySinFun(X_array[1]), MySinFun(X_array[2]), MySinFun(X_array[3]), MySinFun(X_array[4])]

for i in range(N):
    Y_array[i] = round(Y_array[i], rounding)

# Implementing Lagrange Interpolation
def Lagrange(X_array, Y_array, element) -> float:
    PrintVectorAsNp("X", X_array)
    PrintVectorAsNp("Y", Y_array)
    firstPart = f"{Y_array[0]} * ((x - {X_array[1]})/({X_array[0]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[0]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[0]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[0]} - {X_array[4]})) +"
    secondPart = f"{Y_array[1]} * ((x - {X_array[0]})/({X_array[1]} - {X_array[0]})) * ((x - {X_array[2]})/({X_array[1]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[1]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[1]} - {X_array[4]})) +"
    thirdPart = f"{Y_array[2]} * ((x - {X_array[0]})/({X_array[2]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[2]} - {X_array[1]})) * ((x - {X_array[3]})/({X_array[2]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[2]} - {X_array[4]})) +"
    fourthPart = f"{Y_array[3]} * ((x - {X_array[0]})/({X_array[3]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[3]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[3]} - {X_array[2]})) * ((x - {X_array[4]})/({X_array[3]} - {X_array[4]})) +"
    fifthPart = f"{Y_array[4]} * ((x - {X_array[0]})/({X_array[4]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[4]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[4]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[4]} - {X_array[3]}))"
    print(firstPart, secondPart, thirdPart, fourthPart, fifthPart)

    z = 0
    for j in range(len(Y_array)):
        p1 = 1; p2 = 1
        for i in range(len(X_array)):
            if i == j:
                p1 = p1 * 1; p2 = p2 * 1
            else:
                p1 = p1 * (element - X_array[i])
                p2 = p2 * (X_array[j] - X_array[i])
        z = z + Y_array[j] * p1 / p2
    print("Coef of",element,"element =",z)
    return z

Lagrange(X_array, Y_array, X_array[1])
