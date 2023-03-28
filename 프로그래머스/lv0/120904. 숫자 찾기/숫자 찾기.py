def solution(num, k):
    i = str(num).find(str(k))+1
    return i if i>0 else -1