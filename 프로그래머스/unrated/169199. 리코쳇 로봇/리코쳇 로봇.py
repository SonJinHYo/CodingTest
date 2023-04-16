from collections import deque

def after_moving(board,now_pos,direction):
    R,C = len(board),len(board[0])
    r,c = now_pos
    dr,dc = direction
    while (0<=r+dr<R) and (0<=c+dc<C) and (board[r+dr][c+dc]!='D'):
        r,c = r+dr,c+dc
    return (r,c)
    
def solution(board):
    answer = 0
    r,c = 0,0
    move = ((0,1),(1,0),(-1,0),(0,-1))
    for i,row in enumerate(board):
        if 'R' in row:
            r,c = i,row.index('R')
            
    visited = set()
    q = deque([(r,c,0)])
    
    while q:
        now_r,now_c,cnt = q.popleft()
        
        if board[now_r][now_c] == 'G':
            return cnt
        
        if (now_r,now_c) not in visited:
            visited.add((now_r,now_c))
            
            for m in move:
                new_r,new_c = after_moving(board,(now_r,now_c),m)
                q.append((new_r,new_c,cnt+1))
            
    return -1