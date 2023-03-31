def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while(d and d[-1]<=budget):
        answer+=1
        budget-=d.pop()
    return answer