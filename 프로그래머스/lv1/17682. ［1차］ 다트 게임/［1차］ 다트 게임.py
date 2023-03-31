def solution(dartResult):
    answer = 0
    # 문자에 맞는 지수라벨
    label = {'S':1,'D':2,'T':3}
    # 문자열 pop을 위해 역수로 리스트화. 
    dartResult = list(dartResult[::-1])
    # tmp : 만들고있는 수, 직전 수, 전전 수
    tmp = ['',0,0]
    
    # 리스트가 빌 때 까지 반복
    while(dartResult):
        # 이번 문자를 A에 저장
        A = dartResult.pop()
        
        # 숫자라면 현재 숫자에 '문자열'로 더한다. 두 자리수 대비
        if A.isdigit():
            tmp[0] += A
            
        # 알파벳이라면 '현재 숫자**알파벳에 맞는 지수' 를 score에 저장
        elif A.isalpha():
            score = int(tmp[0])**label[A]
            # 현재 만드는 수를 다시 비우고, 방금 더한수, 이전 수 저장
            tmp = ['',score,tmp[1]]
            # 정답에 더해주기
            answer += score
            
        # 옵션 문자가 나왔을 때
        else:
            if A == '*':
                # 바로 전에 더한 수, 그 이전 수를 다시 더하고
                answer += tmp[1]+tmp[2]
                # 해당 숫자들을 2배 해준다.
                tmp[1],tmp[2] = tmp[1]*2,tmp[2]*2
            else:
                # 바로 전에 더한 수를 2배만큼 빼고
                answer-=tmp[1]*2
                # 해당 숫자 부호를 반대로 해준다.
                tmp[1] = -tmp[1]
                
    return answer