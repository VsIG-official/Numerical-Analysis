
matrix=[[1,2,4],[3,-4,1],[2,3,6]]
rightPart=[4,-1,4]
isSquare=True

extendedMatrix=matrix

x=0
while x < len(rightPart):
    extendedMatrix[x].append(rightPart[x])
    x+=1

rows=len(extendedMatrix)
columns=len(extendedMatrix)+1

print(rows)
print(columns)

print(extendedMatrix)

if rows==columns:
   isSquare=True
else:
   isSquare=False
