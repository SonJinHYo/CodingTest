def solution(want, number, discount):
    d = {}
    answer = 0
    for i in range(len(want)):
        d[want[i]] = number[i]
    for i in discount[:10]:
        if i in d:
            d[i]-=1
    if all(True if i<=0 else False for i in d.values()):
        answer+=1
    
    for idx,i in enumerate(discount[10:],start = 10):
        if i in d:
            d[i]-=1
        if discount[idx-10] in d:
            d[discount[idx-10]]+=1
        
        if all(True if i<=0 else False for i in d.values()):
            answer+=1
    return answer
