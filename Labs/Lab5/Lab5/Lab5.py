
# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5
h = 2
numberOfUnknowns = 4

X_array = [3, 5, 7, 9, 11]

countOfX = len(X_array)

# My Sin Function
def MySinFun(x: int, alpha=3) -> float:
    y_value = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return y_value

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

def create_indexes(x_values: list) -> dict:
    indexes = {}
    length = len(x_values)
    for i in range(length - 1):
        indexes[f'b{i + 1}'] = i
        indexes[f'c{i + 1}'] = i + length - 1
        indexes[f'd{i + 1}'] = i + length * 2 - 2
    indexes['y'] = (length - 1) * 3
    return indexes

def CreateMatrixForCramer(X_array, Y_array, indexes) -> [list, list]:
    matrix_a = []
    indexes_length = 13

    for i in range(1, len(X_array)):
        row = np.zeros(indexes_length)
        row[i-1] = h
        row[i+3] = h ** 2
        row[i+7] = h ** 3
        row[12] = Y_array[i] - Y_array[i - 1]
        matrix_a.append(row)

    for i in range(1, len(X_array) - 1):
        row = np.zeros(indexes_length)
        row[i] = 1
        row[i-1] = -1
        row[i+3] = -2 * h
        row[i+7] = -3 * h ** 2
        row[12] = 0
        matrix_a.append(row)

    for i in range(1, len(X_array) - 1):
        row = np.zeros(indexes_length)
        row[i] = 1
        row[i+3] = -1
        row[i+7] = -3 * h
        row[12] = 0
        matrix_a.append(row)

    row = np.zeros(indexes_length)
    row[indexes[f'c{len(X_array) - 1}']] = 1
    row[indexes[f'd{len(X_array) - 1}']] = 3 * (X_array[-1] - X_array[-2])
    row[indexes['y']] = 0
    matrix_a.append(row)
    row = np.zeros(indexes_length)
    row[indexes['c1']] = 1
    row[indexes['y']] = 0
    matrix_a.append(row)
    vector_b = np.zeros(indexes_length - 1)
    for i in range(len(matrix_a)):
        vector_b[i] = matrix_a[i][-1]
    matrix_a = np.delete(matrix_a, np.s_[-1:], axis=1)
    print('Matrix A and vector B')
    print(np.matrix(matrix_a))
    print(vector_b)
    return matrix_a, vector_b

PrintLagrange(X_array, Y_array)

for i in range(N):
    Lagrange(X_array, Y_array, X_array[i], True)
    print("Fault of element", X_array[i], "=", abs(MySinFun(X_array[i]) - Lagrange(X_array, Y_array, X_array[i], False)))

indexes = create_indexes(X_array.copy())

matrix_a, vector_b = CreateMatrixForCramer(X_array.copy(), Y_array.copy(), indexes.copy())
matrix_c = matrix_a.copy()
