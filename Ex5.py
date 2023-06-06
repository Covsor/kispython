import math


def main(y, z, x):
    n = len(x)
    res = 0
    for i in range(n):
        res += (71 * x[i] ** 2 - 69 * z[i] - 72 * y[i//2] ** 3) ** 5
    return 31*res