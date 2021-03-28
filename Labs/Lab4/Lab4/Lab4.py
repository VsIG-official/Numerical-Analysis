# region Starting Values
# need for multiplicating matrices in the end
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[7.25, 0.98, 1.09, 1.105],
          [0.98, 3.17, 1.3, 0.16],
          [1.09, 1.3, 6.43, 2.1],
          [1.105, 0.16, 2.1, 5.11]]

N = len(matrix)
rounding = 6

# endregion Starting Values

# region Identity

def identity(N):
    M = [[0 for x in range(N)] for y in range(N)]
    for i in range(0, N):
        M[i][i] = 1
    return M

# endregion Identity

# region Dot

def dot(matrix1: list, matrix2: list, N: int) -> list:
    res = [[0 for x in range(N)] for y in range(N)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):

                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
                res[i][j] = round(res[i][j], rounding)
    return res

# endregion Dot

# region Prints

# Print vector
def PrintVector(vectorName,vector):
    print("\n",vectorName,"=")
    for i in vector:
        print(i, end = " \t")
    print()

# print matrix
def PrintMatrix(matrixName,matrix):
    print("\n", matrixName,"=")
    for i in matrix:
        for j in i:
            print(j, end=" \t")
            if len(str(j)) <= 5:
                print(end=" \t")
        print()

# print additional parametrs
def PrintParametrs():
    print("\nN =", N)

# just printing
def PrintAll():
    PrintMatrix("Start Matrix", matrix)

    PrintParametrs()

# endregion Prints

PrintAll()

for i in range(N - 1, 0, -1):
    matrix_b = identity(N)

    matrix_b_minus = identity(N)

    # Fill matrix b and minus one b
    for j in range(N):
        if j == i - 1:
            matrix_b[i - 1][j] = round(1 / matrix[i][i - 1], rounding)
        else:
            matrix_b[i - 1][j] = round(matrix[i][j] / matrix[i][i - 1] * (-1), rounding)
        matrix_b_minus[i - 1][j] = round(matrix[i][j], rounding)

    print("\nIteration -", N - i)

    PrintMatrix("Matrix b", matrix_b)

    PrintMatrix("Matrix b minus", matrix_b_minus)

    matrix = dot(matrix_b_minus, dot(matrix, matrix_b, N), N)

    PrintMatrix("Temporary result", matrix)

PrintMatrix("Final result as Frobenius Matrix", matrix)
