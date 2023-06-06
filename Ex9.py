def main(t):
    a = [r[:] for r in t]
    r = [[], [], []]
    for line in a:
        if line[0] is None:
            continue
        r[0].append(line[0].replace('[at]', '@'))
        r[1].append(str(round(float(line[1]), 1)))
        r[2].append(line[3].split(' ')[1])
    return r