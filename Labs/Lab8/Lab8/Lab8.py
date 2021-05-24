
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

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        k1 = h * MyPrimeFunction(x0, y)
        k2 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * MyPrimeFunction(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * MyPrimeFunction(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    return y

print("My variant: y' = e^(-ax)*(y^(2)+b), with y(0) =", yZero, ", intervals = [",leftBorder,",",rightBorder,"] and h =", h)

tempValueForLeftBorder = leftBorder
iterations = 0

print("iterations\t x\t y\t\t\terror")
while tempValueForLeftBorder <= rightBorder + 0.1:
    print(iterations, "\t\t", round(tempValueForLeftBorder, 1), "\t", rungeKutta(leftBorder, yZero, tempValueForLeftBorder, h))
    tempValueForLeftBorder = tempValueForLeftBorder + 0.1
    iterations = iterations + 1
