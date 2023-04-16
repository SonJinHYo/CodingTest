def bingo(board,positions):
    bingo_line = {((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
                 ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
                 ((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))}
    for line in bingo_line:
        if positions & set(line) == set(line):
            return True
    return False
    
def solution(board):
    O_positions = set()
    X_positions = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == "O":
                O_positions.add((r,c))
            elif board[r][c] == "X":
                X_positions.add((r,c))
    
    OX_dif = len(O_positions) - len(X_positions)
    if OX_dif not in (0,1):
        return 0
    else:
        if OX_dif==0 and bingo(board,O_positions):
            return 0
        elif OX_dif==1 and bingo(board,X_positions):
            return 0
    return 1 