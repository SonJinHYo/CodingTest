import numpy as np

def solution(data, col, row_begin, row_end):
    R,C = len(data),len(data[0])
    data.sort(key = lambda x: [x[col-1],-x[0]])
    data = np.array(data,dtype=int)
    S_li = []
    for r in range(row_begin-1,row_end):
        S_li.append(sum(data[r,:]%(r+1)))
    answer = S_li[0]
    for s in S_li[1:]:
        answer = answer ^ s
        
    return int(answer)