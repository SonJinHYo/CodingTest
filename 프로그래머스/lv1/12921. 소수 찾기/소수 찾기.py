def solution(n):
    answer = 0
    
    # 범위 안의 소수를 체크하는 리스트. 소수의 인덱스에 True, 그 외엔 False
    prime_list =[True for _ in range(n+1)]
    # 에라토스테네스의 체 이용. 제일 작은 소수인 2부터 시작
    for i in range(2,n+1):
        # 현재 숫자가 소수라면, 범위안까지 그 배수들을 전부 False. 그리고 answer + 1
        if(prime_list[i]==True):
            for j in range(2*i,n+1,i):
                prime_list[j] = False
            answer+=1            
        
    return answer