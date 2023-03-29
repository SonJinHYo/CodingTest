def solution(common):
    if (common[0]+common[2]) == common[1]*2:
        return common[-1]*2-common[-2]
    else:
        return common[-1]**2//common[-2]
