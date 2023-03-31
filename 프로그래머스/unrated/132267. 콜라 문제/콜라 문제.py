def solution(a, b, n):
    res,answer = 0,0
    while n >= a:
        get = (n//a)*b
        answer += get
        res = n%a
        n = get + res
    return answer