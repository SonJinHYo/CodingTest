from collections import deque
import numpy as np
from math import ceil

def solution(progresses, speeds):
    """ 작업진행률과 작업속도를 받아서, 작업 동시종료 갯수를 반환
    
    Args:
        progresses : 현재 작업진행률 (list)
        speeds : 작업 속도 (list)
        
    return:
        1_D list : 우선 작업이 종료될 시 이후에 동시에 마무리되는 작업의 갯수 리스트
    
    """
    
    # 전처리 과정. 최종적으로 progresses리스트는 ndarray으로 작업종료까지 남은 일수를 원소로 가짐
    prg = np.array(progresses)
    spd = np.array(speeds)
    prg = (100-prg)/spd
    for i in range(len(prg)):
        # 남은 작업일수가 정수가 아니라면 올림을 한다. (ex. 남은 작업일수:6.2 -> 남은 일수:7)
        prg[i] = ceil(prg[i])
    # 첫 예시의 prg : [7. 3. 9.]
    
    # 리턴할 리스트
    result = []
    # 맨 앞 작업부터 빼나갈 것이므로 deque 자료형으로 만든다
    q = deque(prg)
    
    # cnt : 현재 작업 종료시 해결되는 작업 수
    cnt = 1
    # now : 현재 작업의 남은 일수 
    now = q.popleft()
    
    while(q):
        # n : 다음 작업의 남은 일수
        n = q.popleft()
        # 현재 작업이 더 오래 걸린다면 cnt+1
        if now>=n:
            cnt+=1
        # 그렇지 않다면 직전까지의 작업 수를 결과리스트에 넣고
        else:
            result.append(cnt)
            # 현재 작업의 남은 일수를 바꿔준다.
            now=n
            cnt = 1
    result.append(cnt)
    return result
