import math

def solution(n):
    answer = 0
    arr = [False for i in range(n)]
    arr[1] = True
    
    for i in range(2,int(math.sqrt(n))+1):
        
        if (arr[i] == True):
            continue
            
        if ((n-1)%i == 0):
            return i
        
        for j in range(i,n,i):
            arr[j] = True
            
    return n-1