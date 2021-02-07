
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
columns = len(matrix)+1

extendedRows = len(extendedMatrix)
extendedColumns = len(extendedMatrix)+1

PrintAll()

numFactor = 0

# iterating through matrix
for i in range(rows):
    for j in range(i+1,columns):

        k = matrix[i][i]
        l = matrix[j][i]

        if l!=0:
            m = k / l
            print(m)
