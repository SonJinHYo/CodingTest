def solution(s):               # ex. '{{1,2,3},{2,1},{1,2,4,3},{2}}'
    answer = []
    # 앞 뒤의 중괄호들을 잘라준다    ex. '1,2,3},{2,1},{1,2,4,3},{2'
    s = s[2:-2]
    # 중간에 남은 },{ 을 기준으로 잘라서 리스트로 만들어준다
    s_li = s.split('},{')       # ex.['1,2,3','2,1','1,2,4,3','2']
    # 만든 리스트를 길이 기준으로 정렬해서 반복문을 돈다  ['2','2,1','1,2,3','1,2,4,3']
    for li in sorted(s_li,key = lambda x: len(x)):
        # 현재 리스트 내 원소들에서 이미 정답에 들어있는 원소를 제거하여 저장.
        num = set(li.split(',')) - set(answer)
        # 남아있는 문자를 정답에 추가한다.
        answer.append((num.pop()))
    return list(map(int,answer))







