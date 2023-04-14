from math import gcd,ceil

def solution(w,h):
    if w==1 or h==1:
        return 0
    
    total = w*h
    answer = 0
    g = gcd(w,h)
    w //=g
    h //=g
    a = h/w
    sub = 0 
    for x in range(1,w+1):
        sub+=(h-ceil(x*a))
    return total - (w*h-sub*2)*g