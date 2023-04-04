def solution(n):
    arr = [0 for _ in range(n+1)]
    arr[1] = 1
    arr[2] = 2
    # n번째 타일링은, 바로 직전 타일링에서 세로로 하나를 더 붙이거나
    # 전전 타일링에서 가로로 2개 더 붙이는 두 가지 경우가 있으므로 피보나치 수열을 이루게 된다.
    for i in range(3,n+1):
        arr[i] = arr[i-1]+arr[i-2]
        arr[i]%=1000000007
    return arr[-1]%1000000007