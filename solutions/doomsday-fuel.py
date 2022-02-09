import numpy as np

from fractions import Fraction

def solution(m):
    if len(m) < 2: return [1, 1]

    # Absorbing Markov Chain
    # from https://en.wikipedia.org/wiki/Absorbing_Markov_chain
    r, q = split_matrix(m)
    f = np.linalg.inv(np.subtract(np.identity(len(q)), q))
    fr = np.dot(f, r)

    # simplify fractions to smallest
    # common denominator
    result = simplify_fractions(fr[0])

    return result

def split_matrix(m):
    # find absorbing states (rows with null sum)
    absorbing = set()
    for i, row in enumerate(m):
        if sum(row) == 0:
            absorbing.add(i)

    # compute R and Q matrices
    r, q = [], []
    for i, row in enumerate(m):
        if i in absorbing: continue

        row_total = float(sum(row))
        r_row, q_row = [], []
        for j, el in enumerate(row):
            el = el / row_total
            if j in absorbing:
                r_row.append(el)
            else:
                q_row.append(el)

        r.append(r_row)
        q.append(q_row)

    return r, q

def simplify_fractions(l):
    # convert floats to fractions and save
    # numerators and denominators
    nums, denoms = [], []
    for num in l:
        frac = Fraction(num).limit_denominator()
        nums.append(frac.numerator)
        denoms.append(frac.denominator)

    # find the Least Common Multiple (LCM)
    # to use as common denominator
    lcd = 1
    for denom in denoms: lcd = np.lcm(lcd, denom)

    # simplify fractions
    denoms = [lcd / d for d in denoms]
    nums = [n * denoms[i] for i, n in enumerate(nums)]

    return nums + [lcd]
