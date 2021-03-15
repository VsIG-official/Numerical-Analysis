# region Starting Values
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
difference = [0] * N
X = [0] * N
rounding = 6
residualToShow = 3
doOperations = True
epsilonValue = 0.000001 # 10^(-6)
iterations = 0

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

# region Check the results
def Residual():
    multiplied = np.round(np.dot(matrixDiagonal,X),rounding)

    R = np.round(np.subtract(rightPartDiagonal,multiplied),rounding)

    print("R =\n",R)

# endregion Check the results

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

while doOperations:
    tempX = X.copy()
    for i in range(0, N):
        #temporal variable to store rightPart element
        tempVar = rightPartDiagonal[i]

        # calculate every element in array
        for j in range(0, N):
            if(i != j):
                tempVar = tempVar  - (matrixDiagonal[i][j] * X[j])
        # create new value
        X[i] = round(tempVar / matrixDiagonal[i][i], rounding)

    # compare two vectors
    for k in range(N):
        difference[k] = abs(tempX[k] - X[k])
        if max(difference) < epsilonValue:
            doOperations = False

    # show first three iterations of vector X
    if iterations < residualToShow:
        PrintVector("X", X)
    iterations = iterations + 1
    Residual()

PrintVector("X", X)
print("Total iterations = ", iterations)
