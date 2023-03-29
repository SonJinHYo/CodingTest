from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer,denom = numer1*denom2+numer2*denom1,denom1*denom2
    return [numer//gcd(numer,denom),denom//gcd(numer,denom)]