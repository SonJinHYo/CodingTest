from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    d = defaultdict(int)
    for n,y in zip(name,yearning):
        d[n] = y
    for p in photo:
        answer.append(sum([d[i] for i in p]))
        
    return answer