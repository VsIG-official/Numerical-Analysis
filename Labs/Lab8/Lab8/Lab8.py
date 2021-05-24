# region Starting Values
import math

epsilonValue = 0.1
variant = 9
N = K = variant - 5
A = B = 1 + 0.4 * N
h = 0.1
rungeConstants = [0.5, 1, 6, 2]
adamsConstants = [24, 55, 59, 37, 9, 19, 5]
leftBorder = 0
rightBorder = 4
yZero = 0
yFirstAdams = []
ySecondAdams = []
square = half = 2
header = "iterations\t x\t y\t\t\t fault"
rounding = 1
rungeValue = 15
adamsStartValue = 3
numOfIter = 41

# endregion Starting Values

# region Prime Function

def MyPrimeFunction(X, Y):
    result = (Y ** square + B) * math.e ** (-A * X)
    return result

# endregion Prime Function

# region Runge Kutta

def RungeKutta(xInnerZero, yInnerZero, x, h):
    y = yInnerZero
    countToIterate = (int)(x / h)
    for i in range(0, countToIterate):
        K1 = h * MyPrimeFunction(xInnerZero, y)
        K2 = h * MyPrimeFunction(rungeConstants[0] * h + xInnerZero, rungeConstants[0] * K1 + y)
        K3 = h * MyPrimeFunction(rungeConstants[0] * h + xInnerZero, rungeConstants[0] * K2 + y)
        K4 = h * MyPrimeFunction(h + xInnerZero, K3 + y)

        y = (K1 + rungeConstants[3] * K2 + rungeConstants[3] * K3 + K4) * (rungeConstants[1] / rungeConstants[2]) + y

        errorValue = abs((K2 - K3) / (K1 - K2))
        if epsilonValue < errorValue :
            h = h / half

        xInnerZero = xInnerZero + h
    return y

def RungeKuttaFull():
    tempValueForLeftBorder = leftBorder
    iterations = 0
    yFirstRunge = []
    ySecondRunge = []
    print(header)

    # do the Runge's rule
    while tempValueForLeftBorder <= rightBorder + 0.1:
        tempOne = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h)
        yFirstRunge.append(tempOne)
        tempTwo = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h / half)
        ySecondRunge.append(tempTwo)

        faultValue = abs((yFirstRunge[iterations] - ySecondRunge[iterations]) / (rungeValue))

        print(iterations, "\t\t", round(tempValueForLeftBorder, rounding), "\t", tempOne, "\t", "%-.15f"%(faultValue))
        tempValueForLeftBorder = tempValueForLeftBorder + 0.1

        # For Adams Method
        if iterations <= adamsStartValue:
            yFirstAdams.append(yFirstRunge[iterations])
            ySecondAdams.append(ySecondRunge[iterations])

        iterations = iterations + 1

# endregion Runge Kutta

# region Adams

def Adams(firstValuesFromRunge, h):
    iterations = adamsStartValue
    while iterations < ((rightBorder - leftBorder) / h) + 4:
        K4 = MyPrimeFunction(iterations * h - 0.3, firstValuesFromRunge[iterations-3])
        K3 = MyPrimeFunction(iterations * h - 0.2, firstValuesFromRunge[iterations-2])
        K2 = MyPrimeFunction(iterations * h - 0.1, firstValuesFromRunge[iterations-1])
        K1 = MyPrimeFunction(iterations * h, firstValuesFromRunge[iterations])

        firstAdditionalY = h / adamsConstants[0] * (adamsConstants[1] * K1 - adamsConstants[2] * K2 + adamsConstants[3] * K3 - adamsConstants[4] * K4) + firstValuesFromRunge[iterations]
        additionalX = h + h * iterations
        secondAdditionalY = firstValuesFromRunge[iterations] + h / adamsConstants[0] * (adamsConstants[4] * MyPrimeFunction(additionalX, firstAdditionalY) + adamsConstants[5] * K1 - adamsConstants[6] * K2 + K3)

        errorValue = abs(firstAdditionalY - secondAdditionalY)

        if epsilonValue < errorValue :
            h = h / half

        if firstAdditionalY != secondAdditionalY:
            firstValuesFromRunge.append(secondAdditionalY)
        else:
            firstValuesFromRunge.append(firstAdditionalY)

        iterations = iterations + 1
    return firstValuesFromRunge

def AdamsFull():
    print(header)

    yFirstAdamsErrors = Adams(yFirstAdams, h)
    ySecondAdamsErrors = Adams(ySecondAdams, h)
    # do the Runge's rule
    for x in range(numOfIter):
        faultValue = abs((yFirstAdamsErrors[x] - ySecondAdamsErrors[x]) / (rungeValue))
        print(x, "\t\t", round(x * 0.1, rounding), "\t", yFirstAdamsErrors[x], "\t", "%-.15f"%(faultValue))

# endregion Adams

def RunAll():
    print("My variant: y' = e^(-ax)*(y^(2)+b), with y(0) =", yZero, ", intervals = [",leftBorder,",",rightBorder,"] and h =", h)
    print("\nRunge Kutta")
    RungeKuttaFull()
    print("\nAdams")
    AdamsFull()

RunAll()
