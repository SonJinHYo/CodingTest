from collections import Counter

def solution(array):
    cnt = Counter(array).items()
    li = sorted(cnt,key=lambda x: -x[1])
    if len(li)==1:
        return li[0][0]
    return li[0][0] if li[0][1]!=li[1][1] else -1