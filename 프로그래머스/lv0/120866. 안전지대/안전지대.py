from copy import deepcopy

def solution(board):
    check = deepcopy(board)
    R,C = len(board),len(board[0])
    answer = 0
    d = {(1,0),(0,1),(-1,0),(0,-1),
         (1,1),(1,-1),(-1,-1),(-1,1)}
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                for dr,dc in d:
                    if 0<=r+dr<R and 0<=c+dc<C:
                        check[r+dr][c+dc]=1
    for i in check:
        for j in i:
            if j==0:
                answer+=1
    
    return answer