
# region Starting Values

import numpy as np
np.set_printoptions(suppress=True)

rounding = 5
epsilonValue = 0.00001

# endregion Starting Values

def MyFunction(x):
    result = 10 * x ** 5 - 2 * x ** 4 - 4 * x ** 3 + 2 * x + 3
    return result

res = MyFunction(1)
print(res)

def MyPrimeFunction(x):
    result = 50 * x ** 4 - 8 * x ** 3 - 12 * x ** 2 + 2
    return result

res = MyPrimeFunction(1)
print(res)
