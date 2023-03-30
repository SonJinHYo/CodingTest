from queue import PriorityQueue

def solution(n):
    return int(''.join(sorted(str(n),reverse=True)))