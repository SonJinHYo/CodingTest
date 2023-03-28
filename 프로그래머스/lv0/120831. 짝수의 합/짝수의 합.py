def solution(n):
    answer = 0
    return sum(i for i in range(1,n+1) if i%2==0)