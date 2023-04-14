def solution(k, d):
    answer = 0
    x = d - d%k
    d = d**2
    for y in range(0,d+1,k):
        if y**2 > d:
            break
            
        while x**2+y**2 > d and x>0:
            x -= k
        answer += (x//k+1)
        
    return answer