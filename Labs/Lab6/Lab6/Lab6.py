# region Starting Values

epsilonValue = 0.00001
interval = [-0.8, -0.7]
polynomEquation = "10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3"
rootFromMathcad = -0.762158358336533
half = 2

# endregion Starting Values

#region Default Functions

def MyFunction(x):
    func = 10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3
    return func

def MyPrimeFunction(x):
    func = 50 * x ** 4 - 8 * x ** 3 - 12 * x ** 2 + 2
    return func

#endregion Default Functions

#region Methods Functions

def BisectionAndChords(intervals, index):
    numberOfIterations = 0
    for i in intervals:
        # shouldn't be 0
        finalNumber = 1
        firstInterval = intervals[0]
        secondInterval = intervals[1]

        # completion criterion
        while epsilonValue < abs(MyFunction(finalNumber)) and epsilonValue < abs(firstInterval - secondInterval):
            # if 0, then do bisection
            if index == 0:
                finalNumber = (secondInterval + firstInterval) / half
            # else do chords
            else:
                finalNumber = (MyFunction(secondInterval) * firstInterval - MyFunction(firstInterval) * secondInterval) / (MyFunction(secondInterval) - MyFunction(firstInterval))

            if MyFunction(secondInterval) * MyFunction(finalNumber) <= 0:
                firstInterval = finalNumber
            else:
                secondInterval = finalNumber

            numberOfIterations = numberOfIterations + 1

    return finalNumber, numberOfIterations

def Newton(intervals):
    numberOfIterations = 0
    for i in intervals:
        initialXPos = 0
        firstInterval = intervals[0]
        secondInterval = intervals[1]

        # if same symbols (like + && +)
        if MyFunction(firstInterval) * MyPrimeFunction(firstInterval) > 0:
            initialXPos = secondInterval
        # if different symbols (like - && +)
        else:
            initialXPos = firstInterval

        finalNumber = initialXPos - MyFunction(initialXPos) / MyPrimeFunction(initialXPos)
        numberOfIterations = numberOfIterations + 1

        # completion criterion
        while epsilonValue < abs(MyFunction(finalNumber)):
            finalNumber = finalNumber - MyFunction(finalNumber) / MyPrimeFunction(finalNumber)
            numberOfIterations = numberOfIterations + 1

    return finalNumber, numberOfIterations

#endregion Methods Functions

#region Results

print("My Equation", polynomEquation)
print("\nMy Interval", interval)
print("\nMathcad root\n", rootFromMathcad)

print("\nBisection:")
bisectionRoots, bisectionIterations = BisectionAndChords(interval, 0)
print("Root of equation:\n", bisectionRoots, "\nNumber of iterations:\n", bisectionIterations)

print("\nChords:")
chordsRoots, chordsIterations = BisectionAndChords(interval, 1)
print("Root of equation:\n", chordsRoots, "\nNumber of iterations:\n", chordsIterations)

print("\nNewton:")
newtonRoots, newtonIterations = Newton(interval)
print("Root of equation:\n", newtonRoots, "\nNumber of iterations:\n", newtonIterations)

#endregion Results
