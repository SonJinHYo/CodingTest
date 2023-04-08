from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    S = sum(queue1)-sum(queue2)
    for _ in range((len(q1)+len(q2))*2):
        if S>0:
            n = q1.popleft()
            S-=2*n
            q2.append(n)
            ans +=1
            
        elif S<0:
            n = q2.popleft()
            S+=2*n
            q1.append(n)
            ans +=1
        else:
            return ans
        
        
    return -1
            
            
            
