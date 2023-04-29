import heapq 

def solution(jobs):
    answer,now,L = 0,0,0
    start = -1
    heap = []
    
    while(L<len(jobs)):
        for s,d in jobs:
            if start<s<=now:
                heapq.heappush(heap,[d,s])
        if heap:
            dd,ss = heapq.heappop(heap)
            start = now
            now+=dd
            answer+=(now-ss)
            L+=1
        else:
            now+=1
    return answer//len(jobs)
            
    
    
