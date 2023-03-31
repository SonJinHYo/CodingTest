def make_nlist(num):
    li = [0 for _ in range(num+1)]
    for n in range(1,num+1):
        for i in range(n,num+1,n):
            li[i] +=1
    return li

def solution(number, limit, power):
    li = make_nlist(number)[1:]
    
    answer = sum([i if i<=limit else power for i in li])
    return answer