from heapq import heappush,heappop

def solution(n, k, enemy):
    answer = 0
    h = []
    for i,e_n in enumerate(enemy):
        heappush(h,-e_n)
        n-=e_n
        
        if n < 0:
            if k<=0:
                return i
            else:
                n -= heappop(h)
                k -= 1
    return len(enemy)