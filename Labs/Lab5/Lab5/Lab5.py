
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5
indexes_length = 13

differenceBetweenTwoPoints = 2

Xarray = [3, 5, 7, 9, 11]

# My Sin Function
def MySinFun(x: int, alpha=3) -> float:
    element = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return element

Yarray = [MySinFun(Xarray[0]), MySinFun(Xarray[1]), MySinFun(Xarray[2]), MySinFun(Xarray[3]), MySinFun(Xarray[4])]

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
def PrintLagrange(Xarray, Yarray):
    PrintVectorAsNp("X", Xarray)
    PrintVectorAsNp("Y", Yarray)
    print("\nLagrange Polynom:")
    firstPart = f"\n{Yarray[0]} * ((x - {Xarray[1]})/({Xarray[0]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[0]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[0]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[0]} - {Xarray[4]})) +"
    secondPart = f"{Yarray[1]} * ((x - {Xarray[0]})/({Xarray[1]} - {Xarray[0]})) * ((x - {Xarray[2]})/({Xarray[1]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[1]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[1]} - {Xarray[4]})) +"
    thirdPart = f"{Yarray[2]} * ((x - {Xarray[0]})/({Xarray[2]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[2]} - {Xarray[1]})) * ((x - {Xarray[3]})/({Xarray[2]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[2]} - {Xarray[4]})) +"
    fourthPart = f"{Yarray[3]} * ((x - {Xarray[0]})/({Xarray[3]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[3]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[3]} - {Xarray[2]})) * ((x - {Xarray[4]})/({Xarray[3]} - {Xarray[4]})) +"
    fifthPart = f"{Yarray[4]} * ((x - {Xarray[0]})/({Xarray[4]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[4]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[4]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[4]} - {Xarray[3]}))"
    print(firstPart, secondPart, thirdPart, fourthPart, fifthPart, "\n")

# Implementing Lagrange Interpolation
def Lagrange(Xarray, Yarray, pointToShow, show) -> float:
    resultAsYpoint = 0
    for j in range(N):
        tempPoint = 1
        for i in range(N):
            if i != j:
                tempPoint = tempPoint * (pointToShow - Xarray[j])/(Xarray[i] - Xarray[j])
        resultAsYpoint = resultAsYpoint + tempPoint * Yarray[i]
    if show:
        print("Coef of",pointToShow,"element =",resultAsYpoint)
    return resultAsYpoint

def CreateMatrixForCramer(Xarray, Yarray) -> [list, list]:
    matrixForCramer = []

    FirstPartOfEquation(Xarray, Yarray, matrixForCramer)

    SecondPartOfEquation(Xarray, Yarray, matrixForCramer)

    ThirdPartOfEquation(Xarray, Yarray, matrixForCramer)

    FourthPartOfEquation(Xarray, Yarray, matrixForCramer)

    FifthPartOfEquation(Xarray, Yarray, matrixForCramer)

    rightPartForCramer = [0] * (indexes_length - 1)
    for i in range(len(matrixForCramer)):
        rightPartForCramer[i] = matrixForCramer[i][-1]
    matrixForCramer = np.delete(matrixForCramer, np.s_[-1:], axis=1)

    print('Matrix A and vector B')
    print(np.matrix(matrixForCramer))
    print(rightPartForCramer)
    return matrixForCramer, rightPartForCramer

def FirstPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray)):
        queue = [0] * indexes_length
        queue[i-1] = differenceBetweenTwoPoints
        queue[i+3] = differenceBetweenTwoPoints ** 2
        queue[i+7] = differenceBetweenTwoPoints ** 3
        queue[12] = Yarray[i] - Yarray[i - 1]
        matrixForCramer.append(queue)

def SecondPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray) - 1):
        queue = [0] * indexes_length
        queue[i] = 1; queue[i-1] = -1
        queue[i+3] = -2 * differenceBetweenTwoPoints
        queue[i+7] = -3 * differenceBetweenTwoPoints ** 2
        queue[12] = 0
        matrixForCramer.append(queue)

def ThirdPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray) - 1):
        queue = [0] * indexes_length
        queue[i+4] = 1; queue[i+3] = -1
        queue[i+7] = -3 * differenceBetweenTwoPoints
        queue[12] = 0
        matrixForCramer.append(queue)

def FourthPartOfEquation(Xarray, Yarray, matrixForCramer):
    queue = [0] * indexes_length
    queue[7] = 1
    queue[11] = 3 * (Xarray[-1] - Xarray[-2])
    queue[12] = 0
    matrixForCramer.append(queue)

def FifthPartOfEquation(Xarray, Yarray, matrixForCramer):
    queue = [0] * indexes_length
    queue[4] = 1
    queue[12] = 0
    matrixForCramer.append(queue)

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

PrintLagrange(Xarray, Yarray)

for i in range(N):
    Lagrange(Xarray, Yarray, Xarray[i], True)
    print("Fault of element", Xarray[i], "=", abs(MySinFun(Xarray[i]) - Lagrange(Xarray, Yarray, Xarray[i], False)))

matrixForCramer, rightPartForCramer = CreateMatrixForCramer(Xarray.copy(), Yarray.copy())
matrixForComputations = matrixForCramer.copy()
spline_coeffs = solve_kramer_method(matrixForCramer, rightPartForCramer, matrixForComputations)
print(spline_coeffs)