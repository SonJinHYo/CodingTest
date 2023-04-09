def solution(order):
    """오더가 벨트 또는 현재 박스번호와 같을 때 까지 or 박스 번호 다 체크할 때 까지 반복
    박스번호와 같은 경우
        다음 오더
        박스 다음 박스 번호
    박스 번호와 다르고 벨트와 같은 경우
        벨트에서 pop
        다음 오더
    박스 번호, 벨트 다 다른 경우
        현재 박스를 벨트에 append
        다음 박스
    """
    answer = 0
    belt = [-1]
    box_num = 1
    N = len(order)
    order = order[::-1]
    while order and (order[-1] == box_num or order[-1] == belt[-1] or box_num <= N):
        if order[-1] == box_num:
            box_num+=1
            answer+=1
            order.pop()
        elif order[-1] == belt[-1]:
                answer+=1
                belt.pop()
                order.pop()
        else:
            belt.append(box_num)
            box_num+=1
    return answer