from math import gcd

def solution(arr):
    for i in range(1, len(arr)):
        # 여러 수의 최소공배수는 두 수 끼리 최소공배수를 해나간 결과와 같다.
        # 최소공배수 = (두 수의 곱)/(최대공약수)
        arr[i] = arr[i-1] * arr[i] // gcd(arr[i-1], arr[i])
    return arr[-1]