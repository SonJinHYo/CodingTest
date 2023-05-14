from heapq import heappush,heappop

def solution(board):
    L = len(board)
    h = [(0,(0,1),0,0),(0,(1,0),0,0)] # (total_cost,진행방향,row,col)
    move = [(-1,0),(0,1),(1,0),(0,-1),(-1,0),(0,1)]
    idx = {(0,1):1,(1,0):2,(0,-1):3,(-1,0):4}
    cost = [[10**9]*L for _ in range(L)]
    cost[0][0] = 0
    answer = 10**9
    while h:
        total,d,r,c = heappop(h)
        
        if r==c==L-1:
            answer = min(answer,total)
        
        for i,(dr,dc) in enumerate([move[i] for i in [idx[d],idx[d]+1,idx[d]-1]]):
            nxt_r,nxt_c = r+dr,c+dc
            if 0<=nxt_r<L and 0<=nxt_c<L and board[nxt_r][nxt_c] == 0:
                move_cost = 100 if i==0 else 600
                nxt_total = total+move_cost
                if nxt_total <= cost[nxt_r][nxt_c]+400:
                    cost[nxt_r][nxt_c] = nxt_total
                    heappush(h,(nxt_total,(dr,dc),nxt_r,nxt_c))
    return answer