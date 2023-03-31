def solution(survey, choices):
    answer = ''
    # 지표를 딕셔너리로 초기화
    kbti = {'R':0,'T':0,
            'C':0,'F':0,
            'J':0,'M':0,
            'A':0,'N':0}
    
    # 설문지의 인덱스와 왼쪽,오른쪽 문자를 각각 i,L,R 로 저장
    for i,(L,R) in enumerate(survey):
        # 점수가 4보다 작다면, 왼쪽 문자에 (4-점수)를 더해주고
        if choices[i]<4:
            kbti[L]+=4-choices[i]
        # 4보다 크다면, 오른쪽 문자에서 (점수-4)를 더해준다.
        elif choices[i]>4:
            kbti[R]+=choices[i]-4
        # 4일 때는 점수없음
        
    # 둘 씩 비교하기 위해 리스트로 저장해서
    result = list(kbti.items())
    
    # 처음부터 둘 씩 비교해서 더 큰 점수의 문자를 더해준다.
    for i in range(4):
        if result[2*i][1]>=result[2*i+1][1]:
            answer+=result[2*i][0]
        else:
            answer+=result[2*i+1][0]
        
    return answer