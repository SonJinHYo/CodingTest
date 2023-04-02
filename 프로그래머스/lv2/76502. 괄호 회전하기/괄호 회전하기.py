from collections import deque

def isRight(s):
    label = {')':'(','}':'{',']':'['}
    q = deque(s)
    tmp = []
    
    while(q):
        if q[0] in label:
            if not tmp or label[q.popleft()] != tmp[-1]:
                return False
            tmp.pop()
        else:
            tmp.append(q.popleft())
    if tmp:
        return False
    return True


def solution(s):
    if len(s)%2==1:
        return 0
    
    s1 = deque(list(s))
    answer=0
    for _ in range(len(s)):
        if isRight(s1):
            answer+=1
        s1.rotate()
    return answer