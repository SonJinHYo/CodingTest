from collections import Counter

def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += Counter(str(n))[str(k)]
    return answer