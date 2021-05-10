# region Starting Values
import numpy as np
import scipy
import scipy.optimize as opt
from math import cos, sin, factorial

epsilonValue = 0.0001
leftBoard = 0.1
rightBoard = 1.1
defaultNforSimpson = 1
defaultNforGauss = 2

coeffs = {
    1: {'x1': 0.5, 'c1': 2},
    2: {'x1': -0.577350, 'x2': 0.577350, 'c1': 1, 'c2': 1},
    3: {'x1': -0.774597, 'x2': 0, 'x3': 0.774597, 'c1': 0.555555, 'c2': 0.888889, 'c3': 0.555555},
    4: {'x1': -0.861136, 'x2': -0.339981, 'x3': 0.339981, 'x4': 0.861136, 'c1': 0.347855, 'c2': 0.652145,
        'c3': 0.652145, 'c4': 0.347855},
    5: {'x1': -0.906180, 'x2': -0.538470, 'x3': 0, 'x4': 0.538470, 'x5': 0.906180, 'c1': 0.236927, 'c2': 0.478629,
        'c3': 0.568889, 'c4': 0.478629, 'c5': 0.236927},
    6: {'x1': -0.932470, 'x2': -0.661210, 'x3': -0.238620, 'x4': 0.238620, 'x5': 0.661210, 'x6': 0.932470,
        'c1': 0.171324, 'c2': 0.360761,
        'c3': 0.467914, 'c4': 0.467914, 'c5': 0.360761, 'c6': 0.171324},
    7: {'x1': -0.949108, 'x2': -0.741531, 'x3': -0.405845, 'x4': 0, 'x5': 0.405845, 'x6': 0.741531, 'x7': 0.949108,
        'c1': 0.129485, 'c2': 0.279705,
        'c3': 0.381830, 'c4': 0.417960, 'c5': 0.381830, 'c6': 0.279705, 'c7': 0.129485},
    8: {'x1': -0.960290, 'x2': -0.796666, 'x3': -0.525532, 'x4': -0.183434, 'x5': 0.183434, 'x6': 0.525532,
        'x7': 0.796666, 'x8': 0.960290,
        'c1': 0.101228, 'c2': 0.222381,
        'c3': 0.313707, 'c4': 0.362684, 'c5': 0.362684, 'c6': 0.313707, 'c7': 0.222381, 'c8': 0.101228},
}

# endregion Starting Values

#region Default Functions

def MyFunction(x):
    func = cos(x) / (x + 1)
    return func

def ReverseMyFunction(t):
    x = ((t * (rightBoard - leftBoard)) / 2) + ((leftBoard + rightBoard) / 2)
    func = MyFunction(x)
    return func

def MyPrimeFunction(x):
    func = (-sin(x)/(x+1))-(cos(x)/(x+1)**2)
    return func

def MyFourthPrimeFunction(x):
    func = (cos(x)-(4*sin(x)/(x+1))-(12*cos(x)/(x+1)**2)+(24*sin(x)/(x+1)**3)+(24*cos(x)/(x+1)**4))/(x+1)
    return func

def MySixthPrimeFunction(x):
    func=(-cos(x)+(6*sin(x)/(x+1))+(30*cos(x)/(x+1)**2)-(120*sin(x)/(x+1)**3)-(360*cos(x)/(x+1)**4)+(720*sin(x)/(x+1)**5)+(720*cos(x)/(x+1)**6))/(x+1)
    return func

def MyEigthPrimeFunction(x):
    func=(cos(x)-(8*sin(x)/(x+1))-(56*cos(x)/(x+1)**2)+(336*sin(x)/(x+1)**3)+(1680*cos(x)/(x+1)**4)-(6720*sin(x)/(x+1)**5)-(20160*cos(x)/(x+1)**6)+
          (40320*sin(x)/(x+1)**7)+(40320*cos(x)/(x+1)**8))/(x+1)
    return func

def MyTenthPrimeFunction(x):
    func=(-cos(x)+(10*sin(x)/(x+1))+(90*cos(x)/(x+1)**2)-(720*sin(x)/(x+1)**3)-(5040*cos(x)/(x+1)**4)+(30240*sin(x)/(x+1)**5)+(151200*cos(x)/(x+1)**6)
         -(604800*sin(x)/(x+1)**7)-(1814400*cos(x)/(x+1)**8)+(3628800*sin(x)/(x+1)**9)+(3628800*cos(x)/(x+1)**10))/(x+1)
    return func

def MyTwelwethPrimeFunction(x):
    func=(cos(x)-(12*sin(x)/(x+1))-(132*cos(x)/(x+1)**2)+(1320*sin(x)/(x+1)**3)+(1180*cos(x)/(x+1)**4)-(95040*sin(x)/(x+1)**5)
          -(665280*cos(x)/(x+1)**6)+(3991680*sin(x)/(x+1)**7)+(19958400*cos(x)/(x+1)**8)-(79833600*sin(x)/(x+1)**9)-(239500800*cos(x)/
          (x+1)**10)+(479001600*sin(x)/(x+1)**11)+(479001600*cos(x)/(x+1)**12))/(x+1)
    return func

def MyFourteenthPrimeFunction(x):
    func=(-cos(x)+(14*sin(x)/(x+1))+(182*cos(x)/(x+1)**2)-(2184*sin(x)/(x+1)**3)-(24024*cos(x)/(x+1)**4)+(240240*sin(x)/(x+1)**5)+
          (2162160*cos(x)/(x+1)**6)-(17297280*sin(x)/(x+1)**7)-(121080960*cos(x)/(x+1)**8)+(726485760*sin(x)/(x+1)**9)+
          (3632428800*cos(x)/(x+1)**10)-(14529715200*sin(x)/(x+1)**11)-(43589145600*cos(x)/(x+1)**12)+(87178291200*sin(x)/(x+1)**13)
          +(87178291200*cos(x)/(x+1)**14))/(x+1)
    return func

def MySixteenthPrimeFunction(x):
    func=(cos(x)-(16*sin(x)/(x+1))-(240*cos(x)/(x+1)**2)+(3360*sin(x)/(x+1)**3)+(43680*cos(x)/(x+1)**4)-(524160*sin(x)/(x+1)**5)-
          (5765760*cos(x)/(x+1)**6)+(57657600*sin(x)/(x+1)**7)+(518918400*cos(x)/(x+1)**8)-(4151347200*sin(x)/(x+1)**9)-
          (29059430400*cos(x)/(x+1)**10)+(174356582400*sin(x)/(x+1)**11)+(871782912000*cos(x)/(x+1)**12)-(3487131648000*cos(x)/(x+1)**13)
          +(10461394944000*cos(x)/(x+1)**14)+(20922789888000*cos(x)/(x+1)**15)+(20922789888000*cos(x)/(x+1)**16))/(x+1)
    return func

func_list = [MyFourthPrimeFunction, MySixthPrimeFunction, MyEigthPrimeFunction,  MyTenthPrimeFunction, MyTwelwethPrimeFunction,
  MyFourteenthPrimeFunction, MySixteenthPrimeFunction]

#endregion Default Functions

def Simpson(firstInterval, secondInterval):
    N, granic_fault = SimpsonDifference(firstInterval, secondInterval, defaultNforSimpson)
    sum = MyFunction(firstInterval) + MyFunction(secondInterval)
    width = (secondInterval - firstInterval) / (2 * N)
    print("N =", N)
    firstPart = 0
    secondPart = 0
    for i in range(1, N):
        firstPart = firstPart + MyFunction(2 * width * i + firstInterval) * 2
    sum = sum + firstPart
    for i in range(1, N + 1):
        secondPart = secondPart + MyFunction(width * (2 * i - 1) + firstInterval) * 4
    sum = sum + secondPart
    finalResult = sum * width / 3
    return finalResult


def SimpsonDifference(firstInterval, secondInterval, N):
    M = opt.fmin_l_bfgs_b(lambda x: -MyFourthPrimeFunction(x), 1.0, bounds=[(firstInterval, secondInterval)], approx_grad=True)
    fault = abs(M[1][0]) * ((secondInterval - firstInterval) ** 5) / (180 * N ** 4)
    while fault > epsilonValue:
        fault = abs(M[1][0]) * ((secondInterval - firstInterval) ** 5) / (180 * N ** 4)
        N = N + 1
    return N, fault


def Gauss(firstInterval, secondInterval):
    N, granic_fault = GaussDifference(firstInterval, secondInterval, defaultNforGauss)
    print("N =", N)
    result = 0
    for index in range(N):
        result = result + coeffs[N][f'c{index + 1}'] * ReverseMyFunction(coeffs[N][f'x{index + 1}'])
    finalResult = ((secondInterval - firstInterval) / 2) * result
    return finalResult


def GaussDifference(firstInterval, secondInterval, N):
    for func in func_list:
        M = opt.fmin_l_bfgs_b(lambda x: -func(x), 1.0, bounds=[(firstInterval, secondInterval)], approx_grad=True)
        fault = abs(M[1][0]) * (((factorial(N)) ** 4) * (secondInterval - firstInterval) ** (2 * N + 1)) / (
                (2 * N + 1) * (factorial(2 * N)) ** 3)
        if fault < epsilonValue:
            break
        N = N + 1
    return N, fault


print(Simpson(leftBoard, rightBoard))
print(Gauss(leftBoard, rightBoard))