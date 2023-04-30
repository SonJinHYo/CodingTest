def solution(n, s, a, b, fares):
    #시작,a,b
    fare_map = {}
    road_map = {}
    dp = [[10**7 if i!=j else 0 for j in range(n+1)] for i in range(n+1)]
    for i in fares:
        dp[i[0]][i[1]] = i[2]
        dp[i[1]][i[0]] = i[2]

    # k : 경유지
    for k in range(1, n+1):
        # i : 출발지    
        for i in range(1, n+1):
            # j : 목적지
            for j in range(i, n+1):
                if i!=j:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    dp[j][i] = dp[i][j]
        
    answer = 10**10
    for i in range(1,n+1):
        tmp = dp[s][i] + dp[i][b] + dp[i][a]
        answer = min(answer,tmp)
            
    return answer