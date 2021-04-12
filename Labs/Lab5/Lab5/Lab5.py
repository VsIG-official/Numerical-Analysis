
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
    npMatrix = np.array(vector)
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

def CreateMatrixForCramer(X_array, Y_array) -> [list, list]:
    matrix_a = []
    indexes_length = 12
    # I
    for i in range(1, len(x_values)):
        row = np.zeros(indexes_length)
        h = x_values[i] - x_values[i - 1]
        row[indexes[f'b{i}']] = h
        row[indexes[f'c{i}']] = h ** 2
        row[indexes[f'd{i}']] = h ** 3
        row[indexes['y']] = y_values[i] - y_values[i - 1]
        matrix_a.append(row)
    # II
    for i in range(1, len(x_values) - 1):
        row = np.zeros(indexes_length)
        h = x_values[i] - x_values[i - 1]
        row[indexes[f'b{i + 1}']] = 1
        row[indexes[f'b{i}']] = -1
        row[indexes[f'c{i}']] = -2 * h
        row[indexes[f'd{i}']] = -3 * h ** 2
        row[indexes['y']] = 0
        matrix_a.append(row)
    # III
    for i in range(1, len(x_values) - 1):
        row = np.zeros(indexes_length)
        h = x_values[i] - x_values[i - 1]
        row[indexes[f'c{i + 1}']] = 1
        row[indexes[f'c{i}']] = -1
        row[indexes[f'd{i}']] = -3 * h
        row[indexes['y']] = 0
        matrix_a.append(row)
    # IV
    row = np.zeros(indexes_length)
    row[indexes[f'c{len(x_values) - 1}']] = 1
    row[indexes[f'd{len(x_values) - 1}']] = 3 * (x_values[-1] - x_values[-2])
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
    print(template.substitute(string='Matrix A and vector B'))
    print(np.matrix(matrix_a))
    print(vector_b)
    return matrix_a, vector_b