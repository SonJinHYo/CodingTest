def solution(answers):
    answer = []
    # 세 명의 수포자 점수 초기화
    supoja = [0,0,0]
    # 수포자들 각자의 패턴 저장
    pattern= ((1,2,3,4,5),(2,1,2,3,2,4,2,5),(3,3,1,1,2,2,4,4,5,5))
    # 패턴 길이 저장
    pattern_num = (5,8,10)
    
    # k번째 수포자 체크
    for k in range(3):
        for i,ans in enumerate(answers):
            # 수포자의 답과 정답이 같다면 점수 +=1
            if ans==pattern[k][i%pattern_num[k]]:
                supoja[k]+=1
    # 가장 높은 점수 저장
    max_score = max(supoja)
    # 수포자들 점수 중 가장 높은 점수와 같다면 인덱스+1 을 저장해서 리턴
    return [i+1 for i,score in enumerate(supoja) if score==max_score]