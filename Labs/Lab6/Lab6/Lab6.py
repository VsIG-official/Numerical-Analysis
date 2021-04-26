
# region Starting Values

import numpy as np
np.set_printoptions(suppress=True)

rounding = 5
epsilonValue = 0.00001
interval = [-0.7, -0.8]
polynomEquation = "10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3"
polynomCoeffs = [10, -2, -4, 0, 2, 3]
rootFromMathcad = -0.76216

# endregion Starting Values

def MyFunction(x):
    result = 10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3
    return result

def MyPrimeFunction(x):
    result = 50 * x ** 4 - 8 * x ** 3 - 12 * x ** 2 + 2
    return result

def bisectionMethod(intervals, coeffs):
        answers = []
        iterations = 0
        for interval in intervals:
            root = 1000
            a, b = intervals[0], intervals[1]
            while abs(b - a) > epsilonValue and abs(MyFunction(root)) > epsilonValue:
                root = (a + b) / 2
                if MyFunction(root) * MyFunction(a) <= 0:
                    a, b = a, root
                elif MyFunction(root) * MyFunction(b) <= 0:
                    a, b = root, b
                iterations += 1
            answers.append(root)
        print(f'Answers: {answers}, iterations: {iterations}')

bisectionMethod(interval, polynomCoeffs)
