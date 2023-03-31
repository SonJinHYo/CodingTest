import numpy as np

def solution(sizes):
    s = np.array([sorted(i) for i in sizes])
    return int(np.prod(np.max(s,axis=0)))
