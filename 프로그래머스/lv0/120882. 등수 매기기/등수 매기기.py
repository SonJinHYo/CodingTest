def solution(score):
    score_s = sorted([sum(i) for i in score],reverse=True)
    d = {}
    for i,n in enumerate(score_s):
        if n not in d:
            d[n] = i+1
    return [d[sum(i)] for i in score]