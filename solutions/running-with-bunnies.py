from itertools import permutations

def solution(times, times_limit):
    n_bunnies = len(times) - 2
    bunnies = [x for x in range(1, n_bunnies + 1)]

    distances = [bellman_ford(times, src) for src in range(len(times))]
    if has_negative_cycle(distances):
        return [x for x in range(n_bunnies)]

    # try to rescue maximum bunnies first then
    # try less and less until none can be saved
    for i in range(n_bunnies, 0, -1):
        # find the bunny permutations to test them all
        for perm in permutations(bunnies, i):
            # if it is feasible, this is the maximum
            # amount of bunnies we can save
            time = path_time(perm, distances)
            if time <= times_limit:
                return [x - 1 for x in sorted(perm)]
    return []

def has_negative_cycle(graph):
    n_nodes = len(graph)
    distances = graph[0]
    for j in range(n_nodes):
        for k in range(n_nodes):
            weight = graph[j][k]
            if distances[j] + weight < distances[k]:
                return True
    return False

def bellman_ford(graph, src):
    n_nodes = len(graph)
    distances = [float("inf")] * n_nodes
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

def path_time(path, distances):
    # add times for the transitions from the start
    # to the first bunny and from the last to the bulkhead
    first_bunny, last_bunny = path[0], path[-1]
    start, bulkhead = 0, len(distances) - 1
    time = distances[start][first_bunny] + distances[last_bunny][bulkhead]

    # add the times of jumping from bunny to bunny
    for i in range(1, len(path)):
        src, dst = path[i - 1], path[i]
        time += distances[src][dst]

    return time
