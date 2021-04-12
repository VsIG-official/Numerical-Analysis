
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

# print vector
def PrintVectorAsNp(vectorName, vector):
    print("\n", vectorName,"=")
    npMatrix = np.array(vector).round(rounding)
    print(npMatrix.round(rounding))

# print additional parametrs
def PrintParametrs():
    print("\nN =", N)

# endregion Prints

# My Sin Function
def MySinFun(x: int, alpha=3) -> float:
    y_value = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return y_value

X_array = [3, 5, 7, 9, 11]
Y_array = [MySinFun(X_array[0]), MySinFun(X_array[1]), MySinFun(X_array[2]), MySinFun(X_array[3]), MySinFun(X_array[4])]

# Print Lagrange
def PrintLagrange(X_array, Y_array):
    PrintVectorAsNp("X", X_array)
    PrintVectorAsNp("Y", Y_array)
    print("\nLagrange Polynom:")
    firstPart = f"\n{Y_array[0]} * ((x - {X_array[1]})/({X_array[0]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[0]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[0]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[0]} - {X_array[4]})) +"
    secondPart = f"{Y_array[1]} * ((x - {X_array[0]})/({X_array[1]} - {X_array[0]})) * ((x - {X_array[2]})/({X_array[1]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[1]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[1]} - {X_array[4]})) +"
    thirdPart = f"{Y_array[2]} * ((x - {X_array[0]})/({X_array[2]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[2]} - {X_array[1]})) * ((x - {X_array[3]})/({X_array[2]} - {X_array[3]})) * ((x - {X_array[4]})/({X_array[2]} - {X_array[4]})) +"
    fourthPart = f"{Y_array[3]} * ((x - {X_array[0]})/({X_array[3]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[3]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[3]} - {X_array[2]})) * ((x - {X_array[4]})/({X_array[3]} - {X_array[4]})) +"
    fifthPart = f"{Y_array[4]} * ((x - {X_array[0]})/({X_array[4]} - {X_array[0]})) * ((x - {X_array[1]})/({X_array[4]} - {X_array[1]})) * ((x - {X_array[2]})/({X_array[4]} - {X_array[2]})) * ((x - {X_array[3]})/({X_array[4]} - {X_array[3]}))"
    print(firstPart, secondPart, thirdPart, fourthPart, fifthPart, "\n")

# Implementing Lagrange Interpolation
def Lagrange(X_array, Y_array, element, show) -> float:
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
    if show:
        print("Coef of",element,"element =",z)
    return z

PrintLagrange(X_array, Y_array)

for i in range(N):
    Lagrange(X_array, Y_array, X_array[i], True)
    print("Fault of element", X_array[i], "=", abs(MySinFun(X_array[i]) - Lagrange(X_array, Y_array, X_array[i], False)))
