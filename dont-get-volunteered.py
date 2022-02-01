from Queue import PriorityQueue

DELTAS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def next_positions(src):
    (x, y) = (src // 8, src % 8)
    ps = [(x + dx, y + dy) for (dx, dy) in DELTAS]
    ps = [x * 8 + y for (x, y) in ps if x >= 0 and x < 8 and y >= 0 and y < 8]
    return ps

def solution(src, dst):
    if src == dst: return 0

    queue = PriorityQueue()
    queue.put((0, src))

    while not queue.empty():
        (moves, pos) = queue.get()
        for p in next_positions(pos):
            if p == dst: return moves + 1
            queue.put((moves + 1, p))

assert(solution(0, 1) == 3)
assert(solution(19, 36) == 1)
