# region Starting Values
import numpy as np
np.set_printoptions(suppress=True)
from math import sin

rounding = 5
N = 5
numberOfUnknown = 12
lengthOfRowForMatrix = numberOfUnknown + 1

differenceBetweenTwoPoints = 2

Xarray = [3, 5, 7, 9, 11]

# My Sin Function
def MySinFun(x: int, alpha=3) -> float:
    element = sin(alpha / 2 * x) + (x * alpha) ** (1 / 3)
    return element

Yarray = [MySinFun(Xarray[0]), MySinFun(Xarray[1]), MySinFun(Xarray[2]), MySinFun(Xarray[3]), MySinFun(Xarray[4])]

# endregion Starting Values

# region Prints

# Print matrix
def PrintMatrixAsNp(matrixName,matrix):
    print("\n", matrixName,"=")
    npMatrix = np.array(matrix)
    print(npMatrix.round(rounding))

# Print vector
def PrintVectorAsNp(vectorName, vector):
    print("\n", vectorName,"=")
    npMatrix = np.array(vector)
    print(npMatrix.round(rounding))

# Print Lagrange
def PrintLagrange(Xarray, Yarray):
    PrintVectorAsNp("X", Xarray)
    PrintVectorAsNp("Y", Yarray)
    print("\nLagrange Polynom:")
    firstPart = f"\n{Yarray[0]} * ((x - {Xarray[1]})/({Xarray[0]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[0]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[0]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[0]} - {Xarray[4]})) +"
    secondPart = f"{Yarray[1]} * ((x - {Xarray[0]})/({Xarray[1]} - {Xarray[0]})) * ((x - {Xarray[2]})/({Xarray[1]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[1]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[1]} - {Xarray[4]})) +"
    thirdPart = f"{Yarray[2]} * ((x - {Xarray[0]})/({Xarray[2]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[2]} - {Xarray[1]})) * ((x - {Xarray[3]})/({Xarray[2]} - {Xarray[3]})) * ((x - {Xarray[4]})/({Xarray[2]} - {Xarray[4]})) +"
    fourthPart = f"{Yarray[3]} * ((x - {Xarray[0]})/({Xarray[3]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[3]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[3]} - {Xarray[2]})) * ((x - {Xarray[4]})/({Xarray[3]} - {Xarray[4]})) +"
    fifthPart = f"{Yarray[4]} * ((x - {Xarray[0]})/({Xarray[4]} - {Xarray[0]})) * ((x - {Xarray[1]})/({Xarray[4]} - {Xarray[1]})) * ((x - {Xarray[2]})/({Xarray[4]} - {Xarray[2]})) * ((x - {Xarray[3]})/({Xarray[4]} - {Xarray[3]}))"
    print(firstPart, secondPart, thirdPart, fourthPart, fifthPart, "\n")

# endregion Prints

# Implementing Lagrange Interpolation
def Lagrange(X_array, Y_array, pointToShow, show) -> float:
    # Create some prerequisites
    resultAsYpoint = 0
    for k in range(len(Y_array)):
        # Create some prerequisites
        tempPoint1 = 0
        tempPoint2 = 0

        tempPointArray = [tempPoint1, tempPoint2]

        tempPointArray[0] = 1
        tempPointArray[1] = 1

        for m in range(len(X_array)):
            if m == k:
                for z in range(2):
                    tempPointArray[z] = tempPointArray[z] * 1

            else:
                tempPointArray[1] = tempPointArray[1] * (X_array[k] - X_array[m])
                tempPointArray[0] = tempPointArray[0] * (pointToShow - X_array[m])

        resultAsYpoint = resultAsYpoint + Y_array[k] * tempPointArray[0] / tempPointArray[1]

    if show:
        print("Coef of",pointToShow,"element =",resultAsYpoint)

    return resultAsYpoint

def CreateMatrixForCramer(Xarray, Yarray) -> [list, list]:
    # Create some prerequisites
    matrixForCramer = list()
    rightPartForCramer = [0] * (lengthOfRowForMatrix - 1)

    # Call Our functions to create matrix
    FirstPartOfEquation(Xarray, Yarray, matrixForCramer)

    SecondPartOfEquation(Xarray, Yarray, matrixForCramer)

    ThirdPartOfEquation(Xarray, Yarray, matrixForCramer)

    FourthPartOfEquation(Xarray, Yarray, matrixForCramer)

    FifthPartOfEquation(Xarray, Yarray, matrixForCramer)

    # Create Right Part
    for i in range(len(matrixForCramer)):
        rightPartForCramer[i] = matrixForCramer[i][-1]

    # Clean matrix
    matrixForCramer = np.delete(matrixForCramer, np.s_[-1:], axis=1)

    return rightPartForCramer, matrixForCramer

#region PartsOfEquation

def FirstPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray)):
        queue = [0] * lengthOfRowForMatrix

        queue[i-1] = differenceBetweenTwoPoints; queue[i+3] = differenceBetweenTwoPoints ** 2
        queue[i+7] = differenceBetweenTwoPoints ** 3; queue[12] = Yarray[i] - Yarray[i - 1]

        matrixForCramer.append(queue)

def SecondPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray) - 1):
        queue = [0] * lengthOfRowForMatrix

        queue[i] = 1; queue[i-1] = -1; queue[12] = 0
        queue[i+3] = -2 * differenceBetweenTwoPoints; queue[i+7] = -3 * differenceBetweenTwoPoints ** 2

        matrixForCramer.append(queue)

def ThirdPartOfEquation(Xarray, Yarray, matrixForCramer):
    for i in range(1, len(Xarray) - 1):
        queue = [0] * lengthOfRowForMatrix

        queue[i+4] = 1; queue[i+3] = -1; queue[i+7] = -3 * differenceBetweenTwoPoints; queue[12] = 0

        matrixForCramer.append(queue)

def FourthPartOfEquation(Xarray, Yarray, matrixForCramer):
    queue = [0] * lengthOfRowForMatrix

    queue[7] = 1; queue[11] = 3 * differenceBetweenTwoPoints; queue[12] = 0

    matrixForCramer.append(queue)

def FifthPartOfEquation(Xarray, Yarray, matrixForCramer):
    queue = [0] * lengthOfRowForMatrix

    queue[4] = 1; queue[12] = 0

    matrixForCramer.append(queue)

#endregion PartsOfEquation

# Do Cramer Method
def Cramer(matrixForComputations, matrixForCramer, rightPartForCramer) -> list:
    # Create some prerequisites
    SIPcoeffs = list()

    for k in range(0, len(rightPartForCramer)):
        for h in range(0, len(rightPartForCramer)):
            # Get values for right part
            matrixForComputations[h][k] = rightPartForCramer[h]

            if k > 0:
                matrixForComputations[h][k - 1] = matrixForCramer[h][k - 1]

        # Add value to the vector
        SIPcoeffs.append(np.linalg.det(matrixForComputations) / np.linalg.det(matrixForCramer))

        # Rounding values
        SIPcoeffs[k] = round(SIPcoeffs[k], rounding)

    return SIPcoeffs

# Printing Lagrange Equation
PrintLagrange(Xarray, Yarray)

for i in range(N):
    Lagrange(Xarray, Yarray, Xarray[i], True)
    print("Fault of element", Xarray[i], "=", abs(MySinFun(Xarray[i]) - Lagrange(Xarray, Yarray, Xarray[i], False)))

rightPartForCramer, matrixForCramer = CreateMatrixForCramer(Xarray.copy(), Yarray.copy())
matrixForComputations = list(map(list, matrixForCramer))

# Coefficients of spline interpolation polynomials
SIPcoeffs = Cramer(matrixForComputations, matrixForCramer, rightPartForCramer)
PrintVectorAsNp("Coefficients of spline interpolation polynomial", SIPcoeffs)
