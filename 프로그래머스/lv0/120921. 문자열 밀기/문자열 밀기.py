from collections import deque

def solution(A, B):
    if A==B:
        return 0
    qa = deque(A)
    for i in range(len(A)):
        qa.rotate()
        if ''.join(qa)==B:
            return i+1
    return -1