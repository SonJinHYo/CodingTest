def check(r,c,Q_pos):
    for i in Q_pos:
        qr,qc = i[0],i[1]
        if qc==c:
            return False
        if (r+c) == (qr+qc):
            return False
        if (r-c)==(qr-qc):
            return False
    return True
    
def solution(n):
    global answer
    answer = 0
    Q_pos=[]
    
    def dfs(depth):
        if depth==n:
            global answer
            answer+=1
        else:
            for i in range(n):
                if check(depth,i,Q_pos):
                    Q_pos.append([depth,i])
                    dfs(depth+1)
                    Q_pos.pop(-1)
    dfs(0)
    return answer