def solution(left, right):
    return sum([-i if i**0.5==int(i**0.5) else i for i in range(left,right+1)])