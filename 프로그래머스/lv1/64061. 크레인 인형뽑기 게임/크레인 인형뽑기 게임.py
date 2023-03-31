def solution(board, moves):
    # 쌓이게 될 리스트
    tower = []
    answer = 0
    
    # i-1 : 크레인이 뽑을 행.
    for i in moves:
        # 가장 윗 줄(첫 행) 부터 순회하다가
        for j in board:
            # 0이 아닌 행(캐릭터 등장)이 나타나면
            if j[i-1] != 0:
                # 타워에 쌓고 해당 행의 값은 0으로 바꿔준 후 for문 탈출
                tower.append(j[i-1])
                j[i-1] = 0
                break
        # tower에 2개 이상 있고 마지막 두 값이 같다면, 두 개 빼주고 answer+2(점수는 2점씩)
        if len(tower)>1 and tower[-1] == tower[-2]:
            tower.pop()
            tower.pop()
            answer+=2
            
    return answer