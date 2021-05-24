
import math

epsilonValue = 0.1
variant = 9
N = K = variant - 5
A = B = 1 + 0.4 * N
h = 0.1
leftBorder = 0
rightBorder = 4
yZero = 0

def MyPrimeFunction(x, y):
    result = math.e ** (-A * x) * (y ** 2 + B)
    return result

def RungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)(x / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        k1 = h * MyPrimeFunction(x0, y)
        k2 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * MyPrimeFunction(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        fault = abs((k2 - k3) / (k1 - k2))
        if fault > epsilonValue:
            h /= 2
            n = n * 2

        # Update next value of x
        x0 = x0 + h
    return y

def RungeKuttaFull():
    tempValueForLeftBorder = leftBorder
    iterations = 0
    yFirstRunge = []
    ySecondRunge = []
    errors = []
    print("iterations\t x\t y\t\t\terror")
    while tempValueForLeftBorder <= rightBorder + 0.1:
        tempOne = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h)
        yFirstRunge.append(tempOne)
        tempTwo = RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h/2)
        ySecondRunge.append(tempTwo)

        error = (yFirstRunge[iterations] - ySecondRunge[iterations]) / (16 - 1)
        errors.append(error)

        print(iterations, "\t\t", round(tempValueForLeftBorder, 1), "\t", RungeKutta(leftBorder, yZero, tempValueForLeftBorder, h), "\t", errors[iterations])
        tempValueForLeftBorder = tempValueForLeftBorder + 0.1
        iterations = iterations + 1

print("My variant: y' = e^(-ax)*(y^(2)+b), with y(0) =", yZero, ", intervals = [",leftBorder,",",rightBorder,"] and h =", h)

RungeKuttaFull()
