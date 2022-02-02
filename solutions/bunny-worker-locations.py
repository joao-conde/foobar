def solution(x, y):
    diag = x + y - 1
    max_id = sum([i for i in range(1, diag + 1)])
    diag_ids = [i + 1 for i in range(max_id - diag, max_id)]
    return str(diag_ids[x - 1])
