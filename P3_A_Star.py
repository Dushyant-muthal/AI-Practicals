import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            x = state[i] - 1
            h += abs(i // 3 - x // 3) + abs(i % 3 - x % 3)
    return h

def solve(start):
    pq = [(heuristic(start), 0, start)]
    visited = set()
    while pq:
        f, g, state = heapq.heappop(pq)
        if state == goal:
            print("Goal Reached!")
            return
        if state in visited:
            continue
        visited.add(state)
        zero = state.index(0)
        for move in [-3, 3, -1, 1]:
            new_pos = zero + move
            if 0 <= new_pos < 9:
                if move == -1 and zero % 3 == 0:
                    continue
                if move == 1 and zero % 3 == 2:
                    continue
                temp = list(state)
                temp[zero], temp[new_pos] = temp[new_pos], temp[zero]
                new_state = tuple(temp)
                if new_state not in visited:
                    new_g = g + 1
                    heapq.heappush(pq, (new_g + heuristic(new_state), new_g, new_state))
    print("No solution!")

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
print("Initial State:")
print(start[0:3])
print(start[3:6])
print(start[6:9])
solve(start)
