import numpy as np

def solution(citations):
    answer = 0
    
    c = np.array(citations)
    for h in range(1,len(citations)+1):
        up = len((c[(c>=h)]))
        down = len((c[(c<=h)]))
        if up>=h and down<=h:
            answer = h
    return answer