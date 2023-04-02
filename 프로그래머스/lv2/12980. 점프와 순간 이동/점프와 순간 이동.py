def solution(n):
    k=0
    while(n>0):
        while(n%2==0):
            n//=2
        k+=1
        n-=1
    return k