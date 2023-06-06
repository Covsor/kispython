import math


def main(n):
    o = 0
    if n == 0:
        o += -0.61
    elif n == 1:
        o += -0.98
    elif n >= 2:
        o += math.asin(main(n - 1)) / 72 + (1 - main(n - 2)) ** 2 / 19
    return o