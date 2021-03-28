# region Starting Values
# need for multiplicating matrices in the end
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[7.25, 0.98, 1.09, 1.105],
          [0.98, 3.17, 1.3, 0.16],
          [1.09, 1.3, 6.43, 2.1],
          [1.105, 0.16, 2.1, 5.11]]

N = len(matrix)

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

    # explicit for loops
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):

                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]

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
    print("\n",matrixName,"=")
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
    PrintMatrix("Start Matrix",matrix)

    PrintParametrs()

# endregion Prints

PrintAll()

from string import Template
template = Template('#' * 10 + ' $string ' + '#' * 10)

def main_part(matrix_a: list) -> None:
    """
    Get all functions in one place
    :param matrix_a: start matrix
    :return: nothing to return
    """
    normal_form = frobenius(matrix_a)
    print(template.substitute(string='Frobenius form'))
    print(normal_form)

def frobenius(matrix: list) -> list:
    length = len(matrix)
    s_matrix = identity(length)
    for i in range(length - 1, 0, -1):
        matrix_b = identity(length)
        # copy matrix
        matrix_b_minus = list(map(list, matrix_b))

        # Fill matrix b and minus one b
        for j in range(length):
            if j == i - 1:
                matrix_b[i - 1][j] = 1 / matrix[i][i - 1]
            else:
                matrix_b[i - 1][j] = matrix[i][j] / matrix[i][i - 1] * (-1)
            matrix_b_minus[i - 1][j] = matrix[i][j]
        print(template.substitute(string=f'Step: {abs(i - length)}'))
        print(template.substitute(string='Matrix b'))
        print(matrix_b)

        s_matrix = dot(s_matrix, matrix_b, N)

        PrintMatrix('Matrix b minus', matrix_b_minus)

        matrix = dot(matrix_b_minus, dot(matrix, matrix_b, N), N)

        PrintMatrix('Temporary result', matrix)
    return matrix

main_part(matrix.copy())
