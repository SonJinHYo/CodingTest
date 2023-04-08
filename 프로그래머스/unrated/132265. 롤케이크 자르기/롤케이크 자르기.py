from collections import defaultdict,Counter

def solution(topping):
    answer = 0
    r_cnt = defaultdict(int)
    l_cnt = defaultdict(int)
    for t in topping:
        r_cnt[t]+=1
    for t in topping:
        l_cnt[t]+=1
        r_cnt[t]-=1
        if r_cnt[t]==0:
            del r_cnt[t]
        if len(r_cnt)==len(l_cnt):
            answer+=1
    return answer
    
    # for i in range(1,len(topping)-1):
    #     cnt[len(set(topping[:i]))-len(set(topping[i:]))+=1
    # min_index = min(i for i in cnt)
    # return cnt[min_index] 