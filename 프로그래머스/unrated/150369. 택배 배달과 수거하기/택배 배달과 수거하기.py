def after_delive(d_or_c_list,idx,c):
    for _ in range(c):
        d_or_c_list[idx]-=1
        while d_or_c_list[idx]==0:
            if idx == 0:
                return idx-1
            else:
                idx-=1
    return idx

def solution(cap, n, deliveries, pickups):
    d_idx,p_idx = -1,-1
    for i in range(n-1,-1,-1):
        if deliveries[i]!=0:
            d_idx = i
            break
    for i in range(n-1,-1,-1):
        if pickups[i]!=0:
            p_idx = i
            break
    answer = 0
    
    while d_idx >=0 or p_idx >=0:
        answer+=max(d_idx+1,p_idx+1)*2
        d_idx = after_delive(deliveries,d_idx,cap)
        p_idx = after_delive(pickups,p_idx,cap)
    return answer