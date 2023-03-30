def solution(a, b):
    a,b = (b,a) if a>b else (a,b)
    return int((a+b)*(b-a+1)/2)