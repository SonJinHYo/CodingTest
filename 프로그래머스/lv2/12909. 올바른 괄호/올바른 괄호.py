from collections import deque

def solution(s):
    
    q = deque()
    
    for c in s:
        if c==")":
            if not q:
                return False
            q.pop()
        else:
            q.append(c)
    return False if q else True