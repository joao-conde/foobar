def solution(bananas):
    pairs = { i: [] for i, _ in enumerate(bananas) }
    for i, b1 in enumerate(bananas):
        for j, b2 in enumerate(bananas):
            if i == j: continue
            if loops(b1, b2): pairs[i].append(j)

    matches = [item for item in pairs.items() if len(item[1]) > 0]
    matches.sort(key = lambda item: len(item[1]))

    cnt = 0
    while len(matches) > 0:
        (i, ms) = matches[0]
        pick = ms[0]

        matches = [(i, [x for x in xs if x != pick]) for (i, xs) in matches[1:]]
        matches = [(i, xs) for i, xs in matches if len(xs) > 0]
        matches.sort(key = lambda item: len(item[1]))
        cnt += 1

    return len(bananas) - cnt

def loops(i, j):
    n = i + j
    while n % 2 == 0: n /= 2
    return (i % n) != 0

print(solution([1, 1]))
print(solution([1, 7, 3, 21, 13, 19]))
