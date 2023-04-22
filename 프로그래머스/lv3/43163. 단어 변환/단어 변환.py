from collections import deque

def checkWord(w1,w2,k):
    cnt=0
    for i in range(k):
        if w1[i]!=w2[i]:
            cnt+=1
    return cnt == 1

def solution(begin, target, words):
    k = len(begin)
    q = deque([[begin,0]])
    visited = []
    while(q):
        w1,ans = q.popleft()
        
        if w1==target:
            return ans
        
        if not w1 in visited:
            visited.append(w1)
            for w2 in words:
                if not w2 in visited and checkWord(w1,w2,k):
                    q.append([w2,ans+1])
    return 0