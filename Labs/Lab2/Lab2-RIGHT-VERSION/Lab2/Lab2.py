
# need for multiplicating matrices in the end
import numpy as np

# region Starting Values

matrix = [[8.30, 3.42, 4.10, 1.90],
          [3.92, 8.45, 7.98, 2.46],
          [3.77, 8.01, 8.04, 2.28],
          [2.21, 2.85, 1.69, 6.99]]

rightPart =[-9.85, 12.21, 14.65, -8.35]

onesDiagonal = False

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
        print(i, end = ' ')
    print()

# print matrix
def PrintMatrix(matrixName,matrix):
    print("\n",matrixName,"=")
    for i in matrix:
        for j in i:
            print(j, end=" ")
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
for i in range(rows):
    for j in range(i+1,columns):
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

    # Creating temp matrix for correct numbers and indexes
    tempMatrix = list(map(list, extendedMatrix))

    for z in range(i+1):
        for m in tempMatrix:
            del m[0]
    for z in range(i+1):
        del tempMatrix[0]

PrintMatrix("Extended Matrix ",extendedMatrix)

# Make Row Echelon Form
if onesDiagonal == True:
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[j][i] == 0:continue
                topElement = 1
                bottomElement = extendedMatrix[j][i]
                multiplier = topElement / bottomElement
                for k in range(i,extendedColumns):
                    extendedMatrix[j][k] = round(extendedMatrix[j][k] * multiplier, rounding)
    PrintMatrix("Extended Matrix In Row Echelon form",extendedMatrix)

# Search for X
# Back-Substitution
for i in range(rows-1, -1, -1):
    element = extendedMatrix[i][extendedColumns-1]
    for j in range(i+1, extendedColumns-1):
        element -= extendedMatrix[i][j] * X[j]
    finalElement = element / extendedMatrix[i][i]
    X[i] = round(finalElement, rounding)

PrintVector("X",X)
PrintMatrix("Extended Matrix",extendedMatrix)

# region Check the results

multiplied = np.round(np.dot(matrix,X),rounding)

print("Matrix multipled by X =\n",multiplied)

R = np.round(np.subtract(rightPart,multiplied),rounding)

np.set_printoptions(suppress=True)

print("R =\n",R)

# endregion Check the results
