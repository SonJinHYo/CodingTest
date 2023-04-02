from math import log2

def solution(n,a,b):
    a,b = sorted([a,b])
    cnt = 1
    while not (a%2==1 and (a+1)==b):
        n,a,b = map(lambda x:x//2+x%2,[n,a,b])
        cnt+=1
    return cnt