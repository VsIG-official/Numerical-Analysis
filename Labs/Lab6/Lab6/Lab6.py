
# region Starting Values

import numpy as np
np.set_printoptions(suppress=True)

rounding = 5
epsilonValue = 0.00001
interval = [-0.8, -0.7]
polynomEquation = "10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3"
polynomCoeffs = [10, -2, -4, 0, 2, 3]
rootFromMathcad = -0.76216
half = 2

# endregion Starting Values

#region Default Functions

def MyFunction(x):
    result = 10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3
    return result

def MyPrimeFunction(x):
    result = 50 * x ** 4 - 8 * x ** 3 - 12 * x ** 2 + 2
    return result

#endregion Default Functions

#region Methods Functions

def bisectionMethod(intervals):
    numberOfIterations = 0
    for i in intervals:
        numberToStop = epsilonValue * 10 ** 8
        firstInterval = intervals[0]
        secondInterval = intervals[1]
        while abs(MyFunction(numberToStop)) > epsilonValue and abs(secondInterval - firstInterval) > epsilonValue:
            numberToStop = (firstInterval + secondInterval) / half
            if MyFunction(numberToStop) * MyFunction(secondInterval) <= 0:
                firstInterval = numberToStop
            elif MyFunction(numberToStop) * MyFunction(firstInterval) <= 0:
                secondInterval = numberToStop
            numberOfIterations = numberOfIterations + 1
    return numberToStop, numberOfIterations

def newtonMethod(intervals):
    numberOfIterations = 0
    for i in intervals:
        initialXPos = 0
        firstInterval = intervals[0]
        secondInterval = intervals[1]
        if MyFunction(firstInterval) * MyPrimeFunction(firstInterval) > 0:
            initialXPos = firstInterval
        else:
            initialXPos = secondInterval
        numberToStop = initialXPos - MyFunction(initialXPos) / MyPrimeFunction(initialXPos)
        numberOfIterations = numberOfIterations + 1
        while epsilonValue < abs(MyFunction(numberToStop)):
            numberToStop = numberToStop - MyFunction(numberToStop) / MyPrimeFunction(numberToStop)
            numberOfIterations = numberOfIterations + 1
    return numberToStop, numberOfIterations

#endregion Methods Functions

#region Results

print("My Equation", polynomEquation)
print("\nMy Interval", interval)
print("\nMathcad root\n", rootFromMathcad)

print("\nBisection:")
bisectionRoots, bisectionIterations = bisectionMethod(interval)
print("Root of equation:\n", bisectionRoots, "\nNumber of iterations:\n", bisectionIterations)

print("\nNewton:")
newtonRoots, newtonIterations = newtonMethod(interval)
print("Root of equation:\n", newtonRoots, "\nNumber of iterations:\n", newtonIterations)

#endregion Results