from Queue import PriorityQueue

GRID_SIZE = 8

DELTAS = [
    (2, 1),
    (2, -1),
    (-2, 1,),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

def next_positions(src):
    positions = [src + dx * GRID_SIZE + dy for (dx, dy) in DELTAS]
    return [p for p in positions if p >= 0 and p <= 63]

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
