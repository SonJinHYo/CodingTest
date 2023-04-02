def solution(s):
    answer = ''
    # 첫 문자는 대문자
    answer += s[0].upper()
    
    # 이전문자가 공백이라면 대문자, 아니라면 소문자로
    for i in range(1,len(s)):
        if s[i-1]==' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        
    return answer