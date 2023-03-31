def solution(numbers, hand):
    answer = ''
    # 각 전화번호 위치를 딕셔너리로 저장
    pos = {1:(3,0),2:(3,1),3:(3,2),
                   4:(2,0),5:(2,1),6:(2,2),
                   7:(1,0),8:(1,1),9:(1,2),
                   0:(0,1)}
    #현재 내 손 위치 저장
    now_R = (0,0)
    now_L = (0,2)
    
    # 내 손 위치(a) 와 번호위치(b) 사이 거리를 계산해주는 함수
    def distance(a,b):
        return (abs(a[0]-b[0]) + abs(a[1]-b[1]))
    
    for i in numbers:
        # 1,4,7 번호면 왼손, 현재 왼손 위치를 번호 위치로
        if i in [1,4,7]:
            answer+='L'  
            now_L = pos[i]
        # 3,6,9 번호면 오른손, 현재 오른손 위치를 번호 위치로
        elif i in [3,6,9]:
            answer+='R'
            now_R = pos[i]
        # 2,5,8,0 일 때
        else:
            # 왼손잡이 경우
            if hand == 'left':
                # 왼손거리가 더 멀다면 오른손사용
                if distance(pos[i],now_L) > distance(pos[i],now_R):
                    answer+='R'
                    now_R = pos[i]
                # 아니면 왼손
                else:
                    answer+='L'
                    now_L = pos[i]
            # 오른손잡이 경우. 똑같지만 왼손거리가 더 멀거나 같더라도 오른손을 쓰는 차이가 있다.
            else:
                if distance(pos[i],now_L) >= distance(pos[i],now_R):
                    answer+='R'
                    now_R = pos[i]
                else:
                    answer+='L'
                    now_L = pos[i]
            
    return answer
