def solution(n):
    move = {0:(1,0),1:(0,1),2:(-1,-1)}
    arr = [[0]*i for i in range(1,n+1)]
    r,c = -1,0
    num,k = 1,0
    
    for _ in range(n):
        for _ in range(n-k):
            r,c = r+move[k%3][0],c+move[k%3][1]
            arr[r][c] = num
            num+=1
        k+=1
    return [i for row in arr for i in row]
