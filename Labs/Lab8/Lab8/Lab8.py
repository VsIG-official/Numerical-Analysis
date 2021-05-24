import math

epsilonValue = 0.1
variant = 9
N = K = variant - 5
A = B = 1 + 0.4 * N
h = 0.1
leftBorder = 0
rightBorder = 4
yZero = 0
yFirstAdams = []
ySecondAdams = []

def MyPrimeFunction(x, y):
    result = math.e ** (-A * x) * (y ** 2 + B)
    return result

def RungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)(x / h)
    # Iterate for number of iterations
    y = y0
    for i in range(0, n):
        k1 = h * MyPrimeFunction(x0, y)
        k2 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * MyPrimeFunction(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        fault = abs((k2 - k3) / (k1 - k2))
        if fault > epsilonValue:
            h /= 2

        # Update next value of x
        x0 = x0 + h
    return y

def RungeKuttaFull():
    tempValueForLeftBorder = leftBorder
    iterations = 0
    yFirstRunge = []
    ySecondRunge = []
    print("iterations\t x\t y\t\t\t error")

    # do the Runge's rule
    while tempValueForLeftBorder <= rightBorder + 0.1:
        tempOne = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h)
        yFirstRunge.append(tempOne)
        tempTwo = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h / 2)
        ySecondRunge.append(tempTwo)

        error = abs((yFirstRunge[iterations] - ySecondRunge[iterations]) / (15))

        print(iterations, "\t\t", round(tempValueForLeftBorder, 1), "\t", tempOne, "\t", error)
        tempValueForLeftBorder = tempValueForLeftBorder + 0.1

        # For Adams Method
        if iterations <= 3:
            yFirstAdams.append(yFirstRunge[iterations])
            ySecondAdams.append(ySecondRunge[iterations])

        iterations = iterations + 1

def Adams(firstValuesFromRunge, h):
    print("iterations\t x\t y\t\t\t error")
    iterations = 3
    while iterations < ((rightBorder - leftBorder) / h):
        k1 = MyPrimeFunction(h * iterations, firstValuesFromRunge[iterations])
        k2 = MyPrimeFunction(h * iterations - 0.1, firstValuesFromRunge[iterations-1])
        k3 = MyPrimeFunction(h * iterations - 0.2, firstValuesFromRunge[iterations-2])
        k4 = MyPrimeFunction(h * iterations - 0.3, firstValuesFromRunge[iterations-3])
        extra_y = firstValuesFromRunge[iterations] + h / 24 * (55 * k1 - 59 * k2 + 37 * k3 - 9 * k4)
        next_x = h * iterations + h
        intra_y = firstValuesFromRunge[iterations] + h / 24 * (9 * MyPrimeFunction(next_x, extra_y) + 19 * k1 - 5 * k2 + k3)
        fault = abs(intra_y - extra_y)
        if fault > epsilonValue:
            h / 2
        if extra_y == intra_y:
            firstValuesFromRunge.append(extra_y)
        else:
            firstValuesFromRunge.append(intra_y)
        print(iterations-3, "\t\t", round((iterations - 3)* 0.1, 1), "\t", firstValuesFromRunge[iterations-3], "\t")
        iterations = iterations + 1

print("My variant: y' = e^(-ax)*(y^(2)+b), with y(0) =", yZero, ", intervals = [",leftBorder,",",rightBorder,"] and h =", h)
table = []
RungeKuttaFull()
print()
Adams(yFirstAdams, h)
