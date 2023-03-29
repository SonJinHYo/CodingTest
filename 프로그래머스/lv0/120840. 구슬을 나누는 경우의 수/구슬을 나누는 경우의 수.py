from math import factorial as f
def solution(balls, share):
    return f(balls)/(f(share)*f(balls-share))