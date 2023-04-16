from collections import defaultdict

def solution(weights):
    result = 0
    weights.sort(reverse=True)
    d = defaultdict(int)
    
    while weights:
        w = weights.pop()
        result += d[w]        
        possible = [int(i*w) for i in [1,3/2,4/3,2] if i*w==int(i*w)]
        for p in possible:
            d[p] +=1
            
    return result
