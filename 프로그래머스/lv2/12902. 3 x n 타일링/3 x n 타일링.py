def solution(n):
    dp = [0,3,11]
    if n%2 == 1:
        return 0
    else:
        for _ in range(n//2):
            num = 0
            for i in range(len(dp)-1):
                num+=dp[i]
            dp.append((dp[-1]*3+num*2+2)%1000000007)
        print(dp)
    return dp[-3]