def solution(participant, completion):
    # 중복을 제거하고 차집합으로 남는 사람이 있다면
    s1 = set(participant) - set(completion)
    if(s1 != set()):
        # 미완주자이므로 해당 사람을 리턴
        return s1.pop()
    
    # 아니라면 이름 중복이 있는 상황이므로
    else:
        # 각각 정렬해서 같은 인덱스에 다른 이름이 나올 때 이름이 달라진 것
        participant.sort()
        completion.sort()
        for i in range(1,len(completion)):
            if(participant[i]!=completion[i]):
                # 해당 사람을 리턴
                return participant[i]
            
        
