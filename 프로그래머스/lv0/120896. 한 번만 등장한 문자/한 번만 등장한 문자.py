from collections import defaultdict
def solution(s):
    ans = []
    d = defaultdict(int)
    
    for c in s:
        d[c]+=1
    
    for k,v in d.items():
        if v==1:
            ans.append(k)
    return ''.join(sorted(ans))