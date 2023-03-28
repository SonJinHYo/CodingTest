def solution(n):
    answer = 0
    arr = [True for i in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if arr[i]==True:
            for j in range(i*2,n+1,i):
                arr[j]=False
    return n-len([i for i in arr[2:] if i])-1