
# need for multiplicating matrices in the end
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[3.81, 0.25, 1.28, 2.75],
          [2.25, 1.32, 6.58, 0.49],
          [5.31, 8.28, 0.98, 1.04],
          [11.39, 2.45, 3.35, 2.28]]

rightPart = [4.21, 8.47, 2.38, 12.48]

matrixDiagonal =    [[15.2, 4.63, 2.7, 5.03],
                    [2.25, 6.58, 1.32, 0.49],
                    [5.31, 0.98, 8.28, 1.04],
                    [0, 0.119454, -0.426777, 1.48919]]

rightPartDiagonal = [16.69, 8.47, 2.38, 0.026518]

N = len(matrixDiagonal)
zeros = [0] * N
X = [0] * N
rounding = 6

# endregion Starting Values

# copy matrix to create extended matrix
extendedMatrix = list(map(list, matrixDiagonal))

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
    PrintMatrix("Start Matrix",matrix)

    PrintVector("Right Part", rightPart)

    PrintParametrs()

    PrintMatrix("Extended Matrix",extendedMatrix)

# endregion Prints

# add right part to main matrix
RPCounter = 0
while RPCounter < len(rightPartDiagonal):
    extendedMatrix[RPCounter].append(rightPartDiagonal[RPCounter])
    RPCounter += 1

# region Getting rows and columns

rows = len(matrixDiagonal)
columns = len(matrixDiagonal)

extendedRows = len(extendedMatrix)
extendedColumns = len(extendedMatrix)+1

# endregion Getting rows and columns

PrintAll()

for i in range(0, 25):
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, N):
        # temp variable d to store b[j]
        tempVar = rightPartDiagonal[j]

        # to calculate respective xi, yi, zi
        for i in range(0, N):
            if(j != i):
                tempVar=tempVar-(matrixDiagonal[j][i] * X[i])
        # updating the value of our solution
        X[j] = tempVar / matrixDiagonal[j][j]
    print(X)
    # returning our updated solution

# region Check the results

# multiplied = np.round(np.dot(matrixDiagonal,X),rounding)

# print("Matrix multipled by X =\n",multiplied)

# R = np.round(np.subtract(rightPartDiagonal,multiplied),rounding)

# print("R =\n",R)

# endregion Check the results