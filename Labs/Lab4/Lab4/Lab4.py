# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[7.25, 0.98, 1.09, 1.105],
          [0.98, 3.17, 1.3, 0.16],
          [1.09, 1.3, 6.43, 2.1],
          [1.105, 0.16, 2.1, 5.11]]

N = len(matrix)
rounding = 5

# endregion Starting Values

# region Identity

def identity(N):
    matrixForIdentity = [[0 for x in range(N)] for y in range(N)]
    for i in range(0, N):
        matrixForIdentity[i][i] = 1
    return matrixForIdentity

# endregion Identity

# region Dot

def dot(matrix1: list, matrix2: list, N: int) -> list:
    res = [[0 for x in range(N)] for y in range(N)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):

                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res

# endregion Dot

# region Prints

# print matrix
def PrintMatrix(matrixName,matrix):
    print("\n", matrixName,"=")
    for i in matrix:
        for j in i:
            print(round(j, rounding), end=" \t")
            if len(str(j)) <= 6:
                print(end=" \t")
        print()

# print matrix
def PrintMatrixAsNp(matrixName,matrix):
    print("\n", matrixName,"=")
    npMatrix = np.array(matrix)
    print(npMatrix.round(rounding))

# print additional parametrs
def PrintParametrs():
    print("\nN =", N)

# just printing
def PrintAll():
    PrintMatrix("Start Matrix", matrix)

    PrintParametrs()

# endregion Prints

PrintAll()

for x in range(N - 1, 0, -1):
    M_matrix = identity(N)

    M_matrixInverted = identity(N)

    S_matrix = identity(N)
    # Fill matrix b and minus one b
    for y in range(N):
        if y == x - 1:
            M_matrix[x - 1][y] = 1 / matrix[x][x - 1]
        else:
            M_matrix[x - 1][y] = matrix[x][y] / matrix[x][x - 1] * (-1)
        M_matrixInverted[x - 1][y] = matrix[x][y]

    print("\nIteration -", N - x)

    PrintMatrixAsNp("M Matrix", M_matrix)

    S_matrix = dot(S_matrix, M_matrix, N)

    PrintMatrixAsNp("S Matrix", S_matrix)

    PrintMatrixAsNp("M Matrix Inverted", M_matrixInverted)

    matrix = dot(M_matrixInverted, dot(matrix, M_matrix, N), N)

    PrintMatrixAsNp("Temporary result", matrix)

PrintMatrixAsNp("Final result as Frobenius Matrix", matrix)
