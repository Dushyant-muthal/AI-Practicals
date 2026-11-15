def minmax(depth, index, is_max, values, alpha, beta):
    if depth == 3:
        return values[index]
    if is_max:
        best = float("-inf")
        for i in range(2):
            value = minmax(depth + 1, index * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            value = minmax(depth + 1, index * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
result = minmax(0, 0, True, values, float("-inf"), float("inf"))
print("The Optimal solution is:", result)
