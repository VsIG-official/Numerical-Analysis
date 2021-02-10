
# starting values
matrix = [[3,-2,5,0],
          [4,5,8,1],
          [1,1,2,1],
          [2,7,6,5]]

rightPart = [2,4,5,7]

n = len(matrix)
X = [0] * n

# just printing
def PrintAll():
    PrintStartMatrix()

    #PrintParametrs()

    #PrintExtendedMatrix()

    PrintX()

# Print X vector
def PrintX():
    print("X vector = ", X)

def PrintStartMatrix():
    print("Start matrix =")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in matrix]))

# Print extended matrix
def PrintExtendedMatrix():
    print("Extended Matrix =")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in extendedMatrix]))

def PrintParametrs():
    print("Rows =", rows)
    print("Columns =", columns)
    print("n =", n)

PrintAll()

# copy matrix to create extended matrix
extendedMatrix = matrix.copy()

PrintAll()

# add right part to main matrix
RPCounter = 0
while RPCounter < len(rightPart):
    extendedMatrix[RPCounter].append(rightPart[RPCounter])
    RPCounter += 1

PrintAll()

# getting rows and columns
rows = n
columns = n

extendedRows = len(extendedMatrix)
extendedColumns = len(extendedMatrix)+1

#PrintAll()

# Iterating through matrix
# Forward Elimination
for i in range(rows):
    for j in range(i+1,columns):

        if matrix[j][i] == 0:continue
        topElement = extendedMatrix[i][i]
        bottomElement = extendedMatrix[j][i]

        multiplier = topElement / bottomElement

        for k in range(i,extendedColumns):
           extendedMatrix[j][k] = extendedMatrix[i][k] - (extendedMatrix[j][k] * multiplier)

# Search for X
# Back-substitution
for i in range(rows-1, -1, -1):
    element = extendedMatrix[i][extendedColumns-1]
    for j in range(i+1, extendedColumns-1):
        element -= extendedMatrix[i][j] * X[j]
    finalElement = element / extendedMatrix[i][i]
    X[i] = round(finalElement,6)

print(extendedMatrix)
print(X)
