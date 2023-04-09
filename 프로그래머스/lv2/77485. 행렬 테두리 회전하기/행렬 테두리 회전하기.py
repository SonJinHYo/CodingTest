from collections import deque

def solution(rows, columns, queries):
    answer = []
    board = [[row*columns+col+1 for col in range(columns)] for row in range(rows)]
    
    for query in queries:
        rc_li = deque()
        value_li = deque()
        r1,c1,r2,c2 = [i-1 for i in query]
        
        for col in range(c1,c2):
            rc_li.append((r1,col))
            value_li .append(board[r1][col])
        for row in range(r1,r2):
            rc_li.append((row,c2))
            value_li .append(board[row][c2])
        for col in reversed(range(c1+1,c2+1)):
            rc_li.append((r2,col))
            value_li .append(board[r2][col])
        for row in reversed(range(r1+1,r2+1)):
            rc_li.append((row,c1))
            value_li .append(board[row][c1])
            
        rc_li.rotate(-1)
        answer.append(min(value_li))
        for (r,c),v in zip(rc_li,value_li):
            board[r][c] = v
        
    return answer






