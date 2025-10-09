def solve(board):
    print(board)
    count = 0
    while any(r == 0 for row in board for r in row):
        for r in range(4):
            for c in range(4):
                if board[r][c] == 0:
                    cand_r = [board[r][x] for x in range(4) if board[r][x] != 0]
                    cand_c = [board[x][c] for x in range(4) if board[x][c] != 0]

                    cands = set(cand_r + cand_c)
                    answer = [x for x in [1, 2, 3, 4] if x not in cands]
                    
                    if len(answer) == 1:
                        board[r][c] = list(answer)[0]              
        count += 1
        if count > 100:
            return 'This sudoku is unsolvable!'
        
    validates = [
        [board[r+i][c+j] for j in range(2) for i in range(2)] for r in (0, 2) for c in (0, 2)
    ]
    for val in validates:
        if len(val) != len(set(val)):
            return 'This sudoku is unsolvable!'
    return board
            