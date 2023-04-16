def colaz(n):
    if n%2==0:
        return n//2
    else:
        return n*3+1
        

def solution(k, ranges):
    answer = []
    colaz_list = [k]
    while k>1:
        k = colaz(k)
        colaz_list.append(k)
    L = len(colaz_list)
    for s,e in ranges:
        e = L+e
        if s == 0 and e == L:
            answer.append(sum(colaz_list)-colaz_list[0]/2-colaz_list[-1]/2)
        elif s >= e:
            answer.append(-1.0)
        else:
            answer.append(sum(colaz_list[s:e])-colaz_list[s]/2-colaz_list[e-1]/2)
            
    return answer