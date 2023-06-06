import math


def main(b, m, a):
    o = 0
    g = 0
    for k in range(1, b + 1):
        o += k ** 2 - 17 * (math.atan(k ** 2) ** 5)
    for i in range(1, a + 1):
        for j in range(1, m + 1):
            g += (math.sin(68 * i) ** 7 / 8 + 3 * j ** 4 + j ** 2 / 16)
    return o - g