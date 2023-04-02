from collections import deque

def solution(s):
    # 두번째 문자부터 deque에 넣고, s는 첫 문자만 남긴다.
    q = deque(s[1:])
    s = [s[0]]
    
    # q에서 뺴내서 s리스트에 넣는다. 같은 문자가 나타나면 넣지않고 s의 마지막을 뺀다
    while(q):
        char = q.popleft()
        if s and s[-1] ==char:
            s.pop()
        else:
            s.append(char)
            
    # s가 비어있는지 여부에 따라 리턴값을 정해준다.
    if s:
        return 0
    else:
        return 1
