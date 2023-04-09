from heapq import heappush,heappop,heapify
from collections import defaultdict

def solution(N, road, K):
    graph = defaultdict(list)
    for a,b,w in road:
        graph[a].append((w,b))
        graph[b].append((w,a))
    heap = graph[1]
    distance = {1:0}
    heapify(heap)
    
    while(heap):
        w,e = heappop(heap)
        if e not in distance:
            distance[e] = w
            for ww,ee in graph[e]:
                if ee not in distance:
                    heappush(heap,(w+ww,ee))
                    
    cnt = 0
    for dist in distance.values():
        if dist<=K:
            cnt+=1
    return cnt