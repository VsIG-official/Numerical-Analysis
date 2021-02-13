
# need for multiplicating matrices in the end
import numpy as np

# region Starting Values

matrix = [[3,-2,5,0],
          [4,5,8,1],
          [1,1,2,1],
          [2,7,6,5]]

rightPart = [2,4,5,7]

onesDiagonal = True

n = len(matrix)
X = [0] * n

# endregion Starting Values

# copy matrix to create extended matrix
extendedMatrix = list(map(list, matrix))

# region Prints

# Print X vector
def PrintX():
    print("\nX vector = ")
    for i in X:
        print(i, end = ' ')
    print()

# print starting matrix
def PrintMatrix(matrixName,matrix):
    print("\n",matrixName," =")
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

# print right part
def PrintRightPart():
    print("\nRight part of matrix =")
    for i in rightPart:
        print(i, end = ' ')
    print()

# print additional parametrs
def PrintParametrs():
    print("\nRows =", rows)
    print("Columns =", columns)
    print("Exteneded Rows =", extendedRows)
    print("Exteneded Columns =", extendedColumns)
    print("n =", n)

# just printing
def PrintAll():
    PrintMatrix("Start Matrix",matrix)

    PrintRightPart()

    PrintParametrs()

    PrintMatrix("Extended Matrix",extendedMatrix)

    PrintX()

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

# Iterating through matrix
# Forward Elimination without Row Echelon
for i in range(rows):
    for j in range(i+1,columns):

        if matrix[j][i] == 0:continue
        topElement = extendedMatrix[i][i]
        bottomElement = extendedMatrix[j][i]

        multiplier = topElement / bottomElement

        for k in range(i,extendedColumns):
           extendedMatrix[j][k] = extendedMatrix[i][k] - (extendedMatrix[j][k] * multiplier)

PrintMatrix("Extended Matrix",extendedMatrix)

# Do Row Echelon
if onesDiagonal == True:
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[j][i] == 0:continue
                topElement = 1
                bottomElement = extendedMatrix[j][i]
                multiplier = topElement / bottomElement
                for k in range(i,extendedColumns):
                    extendedMatrix[j][k] = extendedMatrix[j][k] * multiplier

# Search for X
# Back-Substitution
for i in range(rows-1, -1, -1):
    element = extendedMatrix[i][extendedColumns-1]
    for j in range(i+1, extendedColumns-1):
        element -= extendedMatrix[i][j] * X[j]
    finalElement = element / extendedMatrix[i][i]
    X[i] = round(finalElement,6)

PrintMatrix("Extended Matrix",extendedMatrix)
PrintX()

# region Check the results

multiplied = np.dot(matrix,X)

print(multiplied)

R = np.subtract(rightPart,multiplied)

np.set_printoptions(suppress=True)

print(R)

# endregion Check the results

