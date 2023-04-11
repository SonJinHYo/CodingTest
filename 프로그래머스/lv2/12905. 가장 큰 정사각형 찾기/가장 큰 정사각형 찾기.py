def solution(board):
    answer = 0
    
    for r in range(1,len(board)):
        for c in range(1,len(board[0])):
            if board[r][c]!=0:
                board[r][c] = min(board[r-1][c],board[r][c-1],board[r-1][c-1])+1
    for r in range(len(board)):
        for c in range(len(board[0])):
            answer = max(board[r][c],answer)
    return answer**2