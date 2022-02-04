def solution(start, length):
    id = start
    checksum = 0
    for skip in range(length):
        for i in range(length - skip):
            checksum ^= (id + i)
        id += length

    return checksum

assert(solution(0, 3) == 2)
assert(solution(17, 4) == 14)
assert(solution(2, 1) == 2)
