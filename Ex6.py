s = ({'LLVM', 1960, 'GDB'},
     {'LLVM', 1960, 'OX'},
     {'LLVM', 1960, 'STATA'},
     {'LLVM', 1990},
     {'LLVM', 2020},
     {'COQ', 'GDB'},
     {'COQ', 'OX'},
     {'COQ', 'STATA', 1960},
     {'COQ', 'STATA', 1990},
     {'COQ', 'STATA', 2020},
     {'LEAN'})


def main(r):
    s1 = set(r)
    mx = [len(i & s1) for i in s]
    a = [i for i, j in enumerate(mx) if j == max(mx)]
    mn = [len(s[i]) for i in a]
    return a[mn.index(min(mn))]