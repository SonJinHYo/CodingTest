def solution(s):
    d = {}
    answer = []
    
    for i,c in enumerate(s):
        if c not in d:
            answer.append(-1)
        else:
            answer.append(i-d[c])
        d[c] = i
    
    return answer