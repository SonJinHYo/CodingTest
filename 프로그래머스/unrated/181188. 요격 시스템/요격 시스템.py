def intersection(s1,s2): # s1의 시작점이 s2의 시작점보다 같거나 작은 상황
    if s1[1] > s2[0]:
        return (max(s1[0],s2[0]),min(s1[1],s2[1]))
    return ()

def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[0])
    inter = [-1,1e9+1]
    for target in targets:
        inter = intersection(inter,target)
        if not inter:
            inter = target
            answer+=1
    return answer
