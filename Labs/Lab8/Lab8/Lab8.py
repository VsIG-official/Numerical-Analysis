# region Starting Values
import math

epsilonValue = 0.1
variant = 9
N = K = variant - 5
A = B = 1 + 0.4 * N
h = 0.1
rungeConstants = [0.5, 1.0, 6.0, 2]
adamsConstants = [24, 55, 59, 37, 9, 19, 5]
leftBorder = 0
rightBorder = 4
yZero = 0
yFirstAdams = []
ySecondAdams = []
half = 2
header = "iterations\t x\t y\t\t\t error"
rounding = 1
rungeValue = 15

# endregion Starting Values

# region Prime Function

def MyPrimeFunction(x, y):
    result = math.e ** (-A * x) * (y ** 2 + B)
    return result

# endregion Prime Function

# region Runge Kutta

def RungeKutta(xInnerZero, yInnerZero, x, h):
    y = yInnerZero
    countToIterate = (int)(x / h)
    for i in range(0, countToIterate):
        K1 = h * MyPrimeFunction(xInnerZero, y)
        K2 = h * MyPrimeFunction(xInnerZero + rungeConstants[0] * h, y + rungeConstants[0] * K1)
        K3 = h * MyPrimeFunction(xInnerZero + rungeConstants[0] * h, y + rungeConstants[0] * K2)
        K4 = h * MyPrimeFunction(xInnerZero + h, y + K3)

        # Update next value of y
        y = y + (rungeConstants[1] / rungeConstants[2])*(K1 + rungeConstants[3] * K2 + rungeConstants[3] * K3 + K4)

        errorValue = abs((K2 - K3) / (K1 - K2))
        if errorValue > epsilonValue:
            h /= half

        # Update next value of x
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

        error = abs((yFirstRunge[iterations] - ySecondRunge[iterations]) / (rungeValue))

        print(iterations, "\t\t", round(tempValueForLeftBorder, rounding), "\t", tempOne, "\t", "%-.15f"%(error))
        tempValueForLeftBorder = tempValueForLeftBorder + 0.1

        # For Adams Method
        if iterations <= 3:
            yFirstAdams.append(yFirstRunge[iterations])
            ySecondAdams.append(ySecondRunge[iterations])

        iterations = iterations + 1

# endregion Runge Kutta

# region Adams

def Adams(firstValuesFromRunge, h):
    iterations = 3
    while iterations < ((rightBorder - leftBorder) / h) + 4:
        K1 = MyPrimeFunction(h * iterations, firstValuesFromRunge[iterations])
        K2 = MyPrimeFunction(h * iterations - 0.1, firstValuesFromRunge[iterations-1])
        K3 = MyPrimeFunction(h * iterations - 0.2, firstValuesFromRunge[iterations-2])
        K4 = MyPrimeFunction(h * iterations - 0.3, firstValuesFromRunge[iterations-3])
        extra_y = firstValuesFromRunge[iterations] + h / adamsConstants[0] * (adamsConstants[1] * K1 - adamsConstants[2] * K2 + adamsConstants[3] * K3 - adamsConstants[4] * K4)
        next_x = h * iterations + h
        intra_y = firstValuesFromRunge[iterations] + h / adamsConstants[0] * (adamsConstants[4] * MyPrimeFunction(next_x, extra_y) + adamsConstants[5] * K1 - adamsConstants[6] * K2 + K3)
        errorValue = abs(intra_y - extra_y)
        if errorValue > epsilonValue:
            h / half
        if extra_y == intra_y:
            firstValuesFromRunge.append(extra_y)
        else:
            firstValuesFromRunge.append(intra_y)
        iterations = iterations + 1
    return firstValuesFromRunge

def AdamsFull():
    print(header)

    yFirstAdamsErrors = Adams(yFirstAdams, h)
    ySecondAdamsErrors = Adams(ySecondAdams, h)
    # do the Runge's rule
    for x in range(41):
        error = abs((yFirstAdamsErrors[x] - ySecondAdamsErrors[x]) / (rungeValue))
        print(x, "\t\t", round(x * 0.1, rounding), "\t", yFirstAdamsErrors[x], "\t", "%-.15f"%(error))

# endregion Adams

def RunAll():
    print("My variant: y' = e^(-ax)*(y^(2)+b), with y(0) =", yZero, ", intervals = [",leftBorder,",",rightBorder,"] and h =", h)
    print("\nRunge Kutta")
    RungeKuttaFull()
    print("\nAdams")
    AdamsFull()

RunAll()
