from collections import deque

def solution(x, y, n):
    answer = 0
    result = 1e9
    q = deque([(y,0)])
    visited = {y}
    
    while q:
        y_min,answer = q.popleft()
        if y_min<x:
            continue
        elif y_min == x:
            return answer
        else:
            y1,y2,y3 = y_min//3,y_min//2,y_min-n
            if y1==y_min/3 and y1 not in visited:
                visited.add(y1)
                q.append((y1,answer+1))
            if y2==y_min/2 and y2 not in visited:
                visited.add(y2)
                q.append((y2,answer+1))
            if y3 not in visited:
                visited.add(y3)
                q.append((y3,answer+1))
    return -1
        
    
