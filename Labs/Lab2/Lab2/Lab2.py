
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
    print("Rows = ", rows)
    print("Columns = ", columns)

    print("Extended Matrix = ", extendedMatrix)

    print("X vector = ", X)

# copy matrix to create extended matrix
extendedMatrix = matrix.copy()

# add right part to main matrix
RPCounter = 0
while RPCounter < len(rightPart):
    extendedMatrix[RPCounter].append(rightPart[RPCounter])
    RPCounter += 1

# getting rows and columns
rows = len(matrix)
columns = len(matrix)

extendedRows = len(extendedMatrix)
extendedColumns = len(extendedMatrix)+1

PrintAll()

# iterating through matrix
for i in range(rows):
    for j in range(i+1,columns):

        if matrix[j][i] == 0:continue
        topElement = extendedMatrix[i][i]
        bottomElement = extendedMatrix[j][i]

        multiplier = topElement / bottomElement

        for k in range(i,extendedColumns):
           extendedMatrix[j][k] = extendedMatrix[i][k] - (extendedMatrix[j][k] * multiplier)

print(extendedMatrix)

print(rows)
print(columns)
print(extendedRows)
print(extendedColumns)

# Search solutions

#for i in range(n-1, -1, -1):
    #X[n-1] = extendedMatrix[i][extendedColumns-1]

    #for j in range(extendedRows+1, extendedColumns-1):
    #    b -= extendedMatrix[i][j] * X[j]
    #x = b / extendedMatrix[i][i]
    #X[i] = x

for i in range(n-1, -1, -1):
    element = extendedMatrix[i][i]
    if element == 0:continue
    for j in range(rows):
        extendedMatrix[i][j] /= element
        for k in range(i):
            extendedMatrix[k][rows] -= extendedMatrix[k][i] * extendedMatrix[i][rows]
            extendedMatrix[k][i] = 0
            X[i] = extendedMatrix[k][rows]
print(X)
print(extendedMatrix)
