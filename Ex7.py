def main(t):
    h2 = int(t[0][1], 16)
    h3 = int(t[1][1], 16)
    h4 = int(t[2][1], 16)
    h5 = int(t[3][1], 16)
    h6 = int(t[4][1], 16)
    r = (((h6 << 6) | h5) << 1) | h4
    r = (((r << 8) | h3) << 9) | h2
    return str(r << 7)