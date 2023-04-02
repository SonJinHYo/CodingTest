from collections import defaultdict

def solution(clothes):
    label = defaultdict(list)
    for v,k in clothes:
        label[k].append(v)
    answer = 1
    for li in label.values():
        answer*=(len(li)+1)
    return answer-1