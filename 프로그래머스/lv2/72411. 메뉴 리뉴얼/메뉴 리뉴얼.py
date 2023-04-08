from collections import Counter,defaultdict
from itertools import combinations

def solution(orders, course):
    answer =  []
    # 각 코스메뉴 갯수마다 체크한다.
    for n in course:
        # M : 최대갯수. 1로 초기화
        M = 1
        # new_menu: 코스요리,나온 갯수를 키,값으로 가지는 딕셔너리
        new_menu = defaultdict(int)
        # 각 메뉴마다 n개씩 조합으로 뽑아서 코스요리 갯수 추가
        for order in orders:
            for o in combinations(sorted(order),n):
                new_menu[o]+=1
        # new_menu가 빌 수도 있으므로 메뉴가 있다면 최댓값을 M으로 갱신
        if new_menu:
            M = max(new_menu.values())
        # 최댓값이 1이라면 코스요리로 쓰지 않으므로 넘어간다
        if M==1:
            continue
        
        # 딕셔너리를 돌며 나타난 횟수가 최댓값이라면 정답리스트에 코스요리 문자열로 대입
        for k,v in new_menu.items():
            if v==M:
                answer.append(''.join(k))

    # 정렬된 정답 리턴                
    return sorted(answer)