def is_solved(board):
    res = {"1": 0, "2": 0}
    if len(set(board[x][x] for x in range(len(board)))) == 1 and board[0][0] != 0:
        res[f"{board[0][0]}"] += 1
    if (
        len(set(board[x][x] for x in range(len(board) - 1, -1, -1))) == 1
        and board[0][0] != 0
    ):
        res[f"{board[-1][-1]}"] += 1

    for x in board:
        if len(set(x)) == 1 and x[0] != 0:
            res[f"{x[0]}"] += 1

    board = list(zip(*board))[::-1]
    for x in board:
        if len(set(x)) == 1 and x[0] != 0:
            res[f"{x[0]}"] += 1
    if res["1"] > res["2"]:
        return 1
    elif res["1"] < res["2"]:
        return 2
    elif res["1"] == res["2"] and res["1"] == 0:
        if any(y == 0 for x in board for y in x):
            return -1
        else:
            return 0
    else:
        return 0
