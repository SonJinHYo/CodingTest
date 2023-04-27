# from collections import deque,Counter

# def solution(n, edge):
#     graph = {}
#     for s,d in edge:
#         graph[s] = graph.get(s,set())|{d}
#         graph[d] = graph.get(d,set())|{s}
#     visited = set()
#     q = deque([1])
#     value = [10000000 for _ in range(n+1)]
#     value[1] = 0
#     while(q):
#         k = q.popleft()
#         if not k in visited:
#             visited.add(k)
#             for i in graph[k]:
#                 if not i in visited:
#                     value[i] = min(value[i],value[k]+1)
#             q+=graph[k]-visited
#     value[0]=0
#     M = max(value)
#     ans = 0
#     for i in value:
#         if M==i:
#             ans+=1
#     return ans

from collections import deque,Counter

def solution(n, edge):
    answer = 0
    maps = {}
    for s,e in edge:
        maps[s] = maps.get(s,set())|{e}
        maps[e] = maps.get(e,set())|{s}
    # print(maps)
    q = deque([1])
    distance = [10000000 for _ in range(n+1)]
    visited = set()
    distance[0] = -1
    distance[1] = 0
    while(q):
        pos = q.popleft()
        if not pos in visited:
            visited.add(pos)
            for nxt_pos in maps[pos]:
                distance[nxt_pos] = min(distance[nxt_pos],distance[pos]+1)
            q+=maps[pos]-visited
    cnt = 0
    M = max(distance)
    for i in distance:
        if i==M:
            cnt+=1
    return cnt












