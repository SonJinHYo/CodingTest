from collections import Counter

def solution(s):
    # 바꾼 0의 갯수, 루프 횟수
    answer,loop = 0,0
    
    # 문제 조건에 맞게 s가 1이 되기 전까지 반복
    while(s != '1'):
        # 0의 갯수를 answer에 더한다.
        answer += Counter(s)['0']
        
        # 모든 0을 제거. 0이 마지막에 있을 경우 빈 칸이 남을 수 있으므로 strip()으로 제거
        s = s.replace('0','').strip()
        
        # 길이를 이진수로. 맨 앞 두문자는 이진수 표기문자 이므로 제거해준다
        s = bin(len(s))[2:]
        # 루프+1
        loop+=1
    return [loop,answer]    