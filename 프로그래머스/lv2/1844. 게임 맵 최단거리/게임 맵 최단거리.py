from collections import deque

def solution(maps):
    R,C = len(maps),len(maps[0])
    move = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
    q = deque([(0,0,1)])
    while(q):
        r,c,ans = q.popleft()
        
        if (r,c) == (R-1,C-1):
            return ans
            
        for i in range(4):
            nxt_r,nxt_c = r+move[i][0],c+move[i][1]
            if 0<=nxt_r<R and 0<=nxt_c<C and maps[nxt_r][nxt_c] == 1:
                maps[nxt_r][nxt_c] = ans
                q.append((nxt_r,nxt_c,ans+1))
                
    return -1