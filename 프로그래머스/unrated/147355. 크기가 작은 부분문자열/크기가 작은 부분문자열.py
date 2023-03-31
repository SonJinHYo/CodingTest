def solution(t, p):
    answer = 0
    P = int(p)
    lt,lp = len(t),len(p)
    
    for i in range(lp,lt+1):
        if int(t[i-lp:i]) <= P:
            answer+=1
    return answer