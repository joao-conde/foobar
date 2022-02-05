def solution(start, length):
    res = 0
    for i in range(length):
        left = start + length * i
        right = left + (length - i) - 1
        res ^= xor_from_zero(right) ^ xor_from_zero(left - 1)
    return res

def xor_from_zero(a):
    m = [a, 1, a + 1, 0]
    return m[a % 4]
