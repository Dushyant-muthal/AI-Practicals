def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
            (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == "X":
            return 1
        if board[a] == board[b] == board[c] == "O":
            return -1
    if " " not in board:
        return 0
    return None

def minimax(board, is_max):
    result = check_winner(board)
    if result is not None:
        return result
    if is_max:
        best = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 2
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)
        return best

def best_move(board):
    best_score, move = -2, -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move

board = [" "] * 9
print("Tic-Tac-Toe: You are O, AI is X")
while True:
    move = best_move(board)
    board[move] = "X"
    print("\nAI played:")
    print_board(board)
    result = check_winner(board)
    if result is not None:
        break
    pos = int(input("Enter position (1-9): ")) - 1
    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move! Try again.")
        board[move] = " "
        continue
    board[pos] = "O"
    result = check_winner(board)
    if result is not None:
        break
print("\nFinal Board:")
print_board(board)
if result == 1:
    print("AI wins!")
elif result == -1:
    print("You win!")
else:
    print("Match Draw!")
