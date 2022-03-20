def solution(times, times_limit):
    bunnies = [x + 1 for x in range(len(times) - 2)]

    distances = [bellman_ford(times, src) for src in range(len(times))]
    if has_negative_cycle(times):
        return range(len(times) - 2)

    return bunnies

def bellman_ford(graph, src):
    n_nodes = len(graph)
    distances = [float("inf")] * len(graph)
    distances[src] = 0

    # as many iterations as there are nodes (at max)
    for _ in range(n_nodes):
        # current starting node
        for j in range(n_nodes):
            # current target node tested if it
            # is shorter to go to it through the
            # current starting node or not
            for k in range(n_nodes):
                weight = graph[j][k]
                if distances[j] + weight < distances[k]:
                    distances[k] = distances[j] + weight

    return distances

def has_negative_cycle(graph):
    n_nodes = len(graph)
    distances = graph[0]
    for j in range(n_nodes):
        for k in range(n_nodes):
            weight = graph[j][k]
            if distances[j] + weight < distances[k]:
                return True
    return False

print(solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]], 1))
# [1, 2]

print(solution([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]], 3))
# [0, 1]
