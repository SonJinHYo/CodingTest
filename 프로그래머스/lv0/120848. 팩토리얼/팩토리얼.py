from math import factorial

def solution(n):
    num,k = 1,1
    while(num<=n):
        num*=k
        k+=1
    return k-2