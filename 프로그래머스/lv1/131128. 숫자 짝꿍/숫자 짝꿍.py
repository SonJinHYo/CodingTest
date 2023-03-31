from collections import defaultdict

def solution(X, Y):
    answer = ''
    d = defaultdict(int)
    
    for c in X:
        d[c]+=1
    
    for c in Y:
        if c in d and d[c]>0:
            answer+=c
            d[c]-=1
    ans = ''.join(sorted(answer,reverse=True))
    if ans=='':
        return '-1'
    elif ans[0] == '0':
        return '0'
    else:
        return ans
