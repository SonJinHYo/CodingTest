def solution(n):
    answer = 0
    
    for s in range(1,n//2+1):
        k = ((1-2*s) + ((2*s-1)**2+8*n)**0.5)/2
        if int(k)==k:
            answer+=1
    return answer+1