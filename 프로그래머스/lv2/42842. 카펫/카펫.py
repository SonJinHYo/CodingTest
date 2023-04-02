def solution(brown, yellow):
    # 세로 최소값 3으로 초기화, 카펫 넓이 선언(타일전체갯수)
    W,S = 3,brown+yellow
    while(True):
        # 가로 길이 = 넓이/세로
        L = S/W
        # 노랑 = (가로-2)*(세로-2), 갈색 = (가로,세로 2배씩 - 4) 이므로 맞는지 확인
        if (yellow,brown) == ((L-2)*(W-2), 2*L+2*W-4):
            # 맞으면 리턴
            return [L,W]
        # 아니면 세로+1
        W+=1
