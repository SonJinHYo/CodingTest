def hanoi(S,D,V,n,answer):
    if (n==1):
        answer.append([S,D])
        return
    hanoi(S,V,D,n-1,answer)
    answer.append([S,D])
    hanoi(V,D,S,n-1,answer)

def solution(n):
    answer = []
    hanoi(1,3,2,n,answer)
    return answer