
# need for multiplicating matrices in the end
import numpy as np
np.set_printoptions(suppress=True)

matrix = [[3.81, 0.25, 1.28, 2.75],
          [2.25, 1.32, 6.58, 0.49],
          [5.31, 8.28, 0.98, 1.04],
          [11.39, 2.45, 3.35, 2.28]]

rightPart = [4.21, 8.47, 2.38, 12.48]

n = len(matrix)
X = [0] * n
rounding = 6

# endregion Starting Values

# copy matrix to create extended matrix
extendedMatrix = list(map(list, matrix))

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
    print(" n =", n)

# just printing
def PrintAll():
    PrintMatrix("Start Matrix",matrix)

    PrintVector("Right Part", rightPart)

    PrintParametrs()

    PrintMatrix("Extended Matrix",extendedMatrix)

# endregion Prints

# add right part to main matrix
RPCounter = 0
while RPCounter < len(rightPart):
    extendedMatrix[RPCounter].append(rightPart[RPCounter])
    RPCounter += 1

# region Getting rows and columns

rows = len(matrix)
columns = len(matrix)

extendedRows = len(extendedMatrix)
extendedColumns = len(extendedMatrix)+1

# endregion Getting rows and columns

PrintAll()

tempMatrix = list(map(list, extendedMatrix))

# Iterating through matrix
# Forward Elimination without Row Echelon
for i in range(1):
    for j in range(1,rows):
        # Getting max number
        maxNum = [max(k, key=abs) for k in zip(*tempMatrix)][0]

        columnArray = [sub[i] for sub in extendedMatrix]

        maxNumIndex = columnArray.index(maxNum)

        # Swapping rows
        firstTempRow = extendedMatrix[:][i]

        rowToChange = extendedMatrix[:][maxNumIndex]

        extendedMatrix[i] = rowToChange
        extendedMatrix[maxNumIndex] = firstTempRow

        # Doing triangular matrix
        if matrix[j][i] == 0:continue
        topElement = extendedMatrix[i][i]
        bottomElement = extendedMatrix[j][i]

        multiplier = topElement / bottomElement

        for k in range(i,extendedColumns):
           extendedMatrix[j][k] = round(extendedMatrix[i][k] - (extendedMatrix[j][k] * multiplier), rounding)

    PrintMatrix("Extended Matrix ",extendedMatrix)


# region Check the results

# multiplied = np.round(np.dot(matrix,X),rounding)

# print("Matrix multipled by X =\n",multiplied)

# R = np.round(np.subtract(rightPart,multiplied),rounding)

# print("R =\n",R)

# endregion Check the results