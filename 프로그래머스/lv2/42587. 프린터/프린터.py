from collections import deque

def solution(priorities, location):
    # 주어진 순서에 맞게 (순위,인덱스) 튜플을 deque로 저장한다.
    q = deque([(val,i) for i,val in enumerate(priorities)])
    # deque([(2, 0), (1, 1), (3, 2), (2, 3)])
        
    # 중요도만 골라서 오름차순 정렬한다
    p_li = sorted(priorities)
    
    # 인쇄된 횟수
    cnt = 0
    while True:
        # 현재 순서의 중요도가 가장 높다면 (중요도 리스트의 마지막값과 같다면)
        if q[0][0]==p_li[-1]:
            # 마지막 중요도 값을 빼면서 cnt+1
            p_li.pop()
            cnt+=1
            # 빼낸 인쇄의 인덱스가 location과 같다면 cnt 리턴
            if q.popleft()[1]==location:
                return cnt
            
        # 중요도가 가장 높지 않다면 rotate(-1) : 맨앞 원소를 맨 뒤로
        else:
            q.rotate(-1)
