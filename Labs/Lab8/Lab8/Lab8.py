
print("My variant: y' = 0.25*y^(2)+x^(2), with y(0) = -1, intervals = [0,0.5] and h = 0.1")

def MyPrimeFunction(x, y):
  result = 0.25*(y*y)+(x*x)
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

# Driver method
x0 = 0
y = -1
x = 0.5
h = 0.1

while x >= 0:
    print ("The value of y (", y, ") at x (", round(x, 1), ") is:", rungeKutta(x0, y, x, h))
    x = x - 0.1
