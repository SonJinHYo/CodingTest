from itertools import combinations

def solution(number):
    answer = 0
    
    for li in combinations(number,3):
        if sum(li)==0:
            answer+=1
    
    return answer