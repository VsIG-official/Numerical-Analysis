
# region Starting Values
# need for multiplicating matrices in the end
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[3.81, 0.25, 1.28, 2.75],
          [2.25, 1.32, 6.58, 0.49],
          [5.31, 8.28, 0.98, 1.04],
          [11.39, 2.45, 3.35, 2.28]]

N = len(matrixDiagonal)
difference = [0] * N
X = [0] * N
rounding = 6
vectorToShow = 3
doOperations = True
epsilonValue = 0.000001 # 10^(-6)
iterations = 0

# endregion Starting Values

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
    print("\n Rows =", rows)
    print(" Columns =", columns)
    print(" Exteneded Rows =", extendedRows)
    print(" Exteneded Columns =", extendedColumns)
    print(" n =", N)

# just printing
def PrintAll():
    PrintMatrix("Start Matrix",matrixDiagonal)

    PrintVector("Right Part", rightPartDiagonal)

    PrintParametrs()

# endregion Prints

# region Getting rows and columns

rows = len(matrixDiagonal)
columns = len(matrixDiagonal)

# endregion Getting rows and columns

PrintAll()