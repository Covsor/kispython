import math


def main(x):
    if (x < 58):
        return 89 * x**2 - x**5 - 45 * (x**3 / 12)**7
    elif (x >= 58 and x < 139):
        return x**2 - 23 * x - x**18
    elif (x >= 139 and x < 158):
        return 3 * x**7 + (x**4 / 16) + (math.ceil(x)**3)**3
    elif (x >= 158 and x < 228):
        return 44 + 89 * x**5
    elif (x >= 228):
        return 7 * x**5 - 11 * x**2