N = 8
board = [-1] * N

def safe(row, col):
    for c in range(col):
        if board[c] == row or abs(board[c] - row) == abs(c - col):
            return False
    return True

def solve(col):
    if col == N:
        return True
    for row in range(N):
        if safe(row, col):
            board[col] = row
            if solve(col + 1):
                return True
            board[col] = -1
    return False

if solve(0):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print()
else:
    print("No solution")
