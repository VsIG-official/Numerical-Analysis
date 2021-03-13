
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





# region Check the results

multiplied = np.round(np.dot(matrix,X),rounding)

print("Matrix multipled by X =\n",multiplied)

R = np.round(np.subtract(rightPart,multiplied),rounding)

np.set_printoptions(suppress=True)

print("R =\n",R)

# endregion Check the results