from collections import deque

def bfs_8_puzzle(start, goal):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    move_taken = {start: None}
    while q:
        state = q.popleft()
        if state == goal:
            path, moves = [], []
            current = state
            while current is not None:
                path.append(current)
                if move_taken[current] is not None:
                    moves.append(move_taken[current])
                current = parent[current]
            return path[::-1], moves[::-1]
        zero = state.index(0)
        row, col = divmod(zero, 3)
        for dr, dc, move in [(-1, 0, "Up"), (1, 0, "Down"),
                             (0, -1, "Left"), (0, 1, "Right")]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                ni = nr * 3 + nc
                temp = list(state)
                temp[zero], temp[ni] = temp[ni], temp[zero]
                nxt = tuple(temp)
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = state
                    move_taken[nxt] = move
                    q.append(nxt)
    return None, None

def show(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
path, moves = bfs_8_puzzle(start, goal)
print("BFS 8-Puzzle")
print("Initial State:")
show(start)
print("\nGoal State:")
show(goal)
if path:
    print("\nSolution found: Yes")
    print("Number of moves:", len(moves))
    for i, state in enumerate(path):
        print("Step", i)
        show(state)
    print("Moves:", moves)
else:
    print("No solution exists.")
