
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5
indexes_length = 13

differenceBetweenTwoPoints = 2

X_array = [3, 5, 7, 9, 11]

# My Sin Function
def MySinFun(x: int, alpha=3) -> float:
    element = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return element

Y_array = [MySinFun(X_array[0]), MySinFun(X_array[1]), MySinFun(X_array[2]), MySinFun(X_array[3]), MySinFun(X_array[4])]

# region Prints

# print matrix
def PrintMatrixAsNp(matrixName,matrix):
    print("\n", matrixName,"=")
    npMatrix = np.array(matrix)
    print(npMatrix.round(rounding))

# print vector
def PrintVectorAsNp(vectorName, vector):
    print("\n", vectorName,"=")
    npMatrix = np.array(vector)
    print(npMatrix.round(rounding))

# endregion Prints

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
def Lagrange(X_array, Y_array, pointToShow, show) -> float:
    resultAsYpoint = 0
    for j in range(N):
        tempPoint = 1
        for i in range(N):
            if i != j:
                tempPoint = tempPoint * (pointToShow - X_array[j])/(X_array[i] - X_array[j])

        resultAsYpoint = resultAsYpoint + tempPoint * Y_array[i]
    if show:
        print("Coef of",pointToShow,"element =",resultAsYpoint)
    return resultAsYpoint

def CreateMatrixForCramer(X_array, Y_array) -> [list, list]:
    matrixForCramer = []

    AssignFirstFour(X_array, Y_array, matrixForCramer)

    for i in range(1, len(X_array) - 1):
        row = [0] * indexes_length
        row[i] = 1
        row[i-1] = -1
        row[i+3] = -2 * differenceBetweenTwoPoints
        row[i+7] = -3 * differenceBetweenTwoPoints ** 2
        row[12] = 0
        matrixForCramer.append(row)

    for i in range(1, len(X_array) - 1):
        row = [0] * indexes_length
        row[i+4] = 1
        row[i+3] = -1
        row[i+7] = -3 * differenceBetweenTwoPoints
        row[12] = 0
        matrixForCramer.append(row)

    row = [0] * indexes_length
    row[i+4] = 1
    row[i+8] = 3 * (X_array[-1] - X_array[-2])
    row[12] = 0
    matrixForCramer.append(row)
    row = [0] * indexes_length
    row[i+1] = 1
    row[12] = 0
    matrixForCramer.append(row)
    rightPartForCramer = [0] * (indexes_length - 1)
    for i in range(len(matrixForCramer)):
        rightPartForCramer[i] = matrixForCramer[i][-1]
    matrixForCramer = np.delete(matrixForCramer, np.s_[-1:], axis=1)
    print('Matrix A and vector B')
    print(np.matrix(matrixForCramer))
    print(rightPartForCramer)
    return matrixForCramer, rightPartForCramer

def AssignFirstFour(X_array, Y_array, matrixForCramer):
    for i in range(1, len(X_array)):
        row = [0] * indexes_length
        row[i-1] = differenceBetweenTwoPoints
        row[i+3] = differenceBetweenTwoPoints ** 2
        row[i+7] = differenceBetweenTwoPoints ** 3
        row[12] = Y_array[i] - Y_array[i - 1]
        matrixForCramer.append(row)

def solve_kramer_method(matrixForCramer, rightPartForCramer, matrixForComputations) -> list:
    spline_coeffs = []
    for i in range(0, len(rightPartForCramer)):
        for j in range(0, len(rightPartForCramer)):
            matrixForComputations[j][i] = rightPartForCramer[j]
            if i > 0:
                matrixForComputations[j][i - 1] = matrixForCramer[j][i - 1]
        spline_coeffs.append(np.linalg.det(matrixForComputations) / np.linalg.det(matrixForCramer))
    spline_coeffs = np.array(spline_coeffs).round(5)
    return spline_coeffs

PrintLagrange(X_array, Y_array)

for i in range(N):
    Lagrange(X_array, Y_array, X_array[i], True)
    print("Fault of element", X_array[i], "=", abs(MySinFun(X_array[i]) - Lagrange(X_array, Y_array, X_array[i], False)))

matrixForCramer, rightPartForCramer = CreateMatrixForCramer(X_array.copy(), Y_array.copy())
matrixForComputations = matrixForCramer.copy()
spline_coeffs = solve_kramer_method(matrixForCramer, rightPartForCramer, matrixForComputations)
print(spline_coeffs)