def solution(n):
    fib = [0,1]
    for i in range(n-1):
        # 마지막 두 항을 더한 값을 append 해준다
        fib.append((fib[-1]+fib[-2])%1234567)
    return fib[-1]