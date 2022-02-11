def solution(m, f):
    m, f, cycles = int(m), int(f), 0
    while m > 0 and f > 0:
        steps = max(m, f) // min(m, f)
        cycles += steps
        if m > f:
            m -= f * steps
        else:
            f -= m * steps
    return str(cycles - 1) if m == 1 or f == 1 else "impossible"
