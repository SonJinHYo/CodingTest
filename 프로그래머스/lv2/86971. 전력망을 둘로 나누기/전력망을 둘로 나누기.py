from collections import defaultdict

def solution(n, wires):
    answer = 1000
    for i in range(n-1):
        graph = defaultdict(list)
        for s,e in (wires[:i]+wires[i+1:]):
            graph[s].append(e)
            graph[e].append(s)
        
        visited = []
        stack= [1]
        while(stack):
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack+=graph[node]
                
        answer = min(answer,abs(n-2*len(visited)))
        
    return answer