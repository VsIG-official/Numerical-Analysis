
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
extendedMatrix = matrix

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

numFactor = 0

# iterating through matrix
for i in range(rows):
    for j in range(i+1,columns):

        if matrix[i][j] == 0:
            continue
        topElement = extendedMatrix[i][i]
        bottomElement = extendedMatrix[j][i]

        factor = topElement / bottomElement
        print(factor)

        for k in range(i,extendedColumns):
           extendedMatrix[j][k] = extendedMatrix[i][k] - (extendedMatrix[j][k] * factor)

           #print(extendedMatrix[j][k])
           #print("i=",i,"j=",j,"k=",k)
           print(extendedMatrix)

