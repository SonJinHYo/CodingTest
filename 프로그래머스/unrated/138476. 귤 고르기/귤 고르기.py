from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    cnt = defaultdict(int)
    
    for n in tangerine:
        cnt[n]+=1
    
    cnt_list = sorted(cnt.items(),key = lambda x: -x[1])
    
    while k>0:
        k -= cnt_list[answer][1]
        answer+=1
    
    return answer