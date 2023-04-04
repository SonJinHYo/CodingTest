from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 던전이 8개 뿐이므로 순열의 수를 탐색한다. (8! = 4만 정도)
    for d in permutations(dungeons):
        d = list(d)
        cnt,kk = 0,k
        while(d and kk>=d[-1][0]):
            kk-=d[-1][1]
            d.pop()
            cnt+=1
        answer = max(answer,cnt)
    return answer