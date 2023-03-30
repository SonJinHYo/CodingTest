from math import sqrt
def solution(n):
    return (sqrt(n)+1)**2 if sqrt(n) == int(sqrt(n)) else -1
