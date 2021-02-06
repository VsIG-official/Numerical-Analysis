
# starting values
matrix = [[3,-2,5,0],
        [4,5,8,1],
        [1,1,2,1],
        [2,7,6,5]]

rightPart = [2,4,5,7]

n = len(matrix)
X = [0] * n

# copy matrix to create extended matrix
extendedMatrix = matrix

# add right part to main matrix
RPCounter = 0
while RPCounter < len(rightPart):
    extendedMatrix[RPCounter].append(rightPart[RPCounter])
    RPCounter += 1

# getting rows and columns
rows = len(extendedMatrix)
columns = len(extendedMatrix)+1

# just printing
print("Rows = ", rows)
print("Columns = ", columns)

print("Extended Matrix = ", extendedMatrix)

print("X vector = ", X)
