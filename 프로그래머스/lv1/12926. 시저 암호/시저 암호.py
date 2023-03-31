def solution(s, n):
    answer = ''
    for i in s:
        # 문자가 a~z 라면
        if ('a'<=i<='z'):
            # 그리고 n만큼 더했을 때 z보다 크다면, n을 더한 값에 알파벳 길이(26) 만큼 빼준다. 
            if ord(i)+n >ord('z'):
                answer += chr((ord(i)+n)-26)
            # 작다면, n을 더하기만 해준다
            else:
                answer += chr((ord(i)+n))
                
        # 이하는 같은 과정
        elif ('A'<=i<='Z'):
            if ord(i)+n >ord('Z'):
                answer += chr((ord(i)+n)-26)
            else:
                answer += chr((ord(i)+n))
        # 공백이면 그냥 공백
        else:
            answer += ' '
    return answer