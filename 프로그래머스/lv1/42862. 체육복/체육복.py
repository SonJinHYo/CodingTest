from collections import Counter

def solution(n, lost, reserve):
    # 체육복 현황 리스트. i 가 여벌명단에 있으면 2, 없으면 1을 리턴
    clothes = [2 if i in reserve else 1 for i in range(n+2)]
    # 처음과 마지막은 좌,우를 살필 때 첫사람과 끝 사람을 위해 만들어 둠. 0으로 초기화를 한다.
    clothes[0],clothes[-1] = 0,0
    # 잃어버린 사람들은 1을 빼준다. clothes(체육복 현황) 완성.
    for i in lost:
        clothes[i]-=1
    
    # 처음과 끝을 제외하면서 순회
    for i in range(1,n+1):
        # 만약 체육복이 없다면
        if clothes[i]==0:
            # 좌우 순서로 체육복 여벌이 있는지 확인하고 빌리기. (빌린 사람,빌려준 사람 == 1,1)
            
            if clothes[i-1]==2:
                clothes[i-1],clothes[i]= 1,1
            elif clothes[i+1]==2:
                clothes[i],clothes[i+1]= 1,1
    
    # 0 갯수 세기. 반복문으로 세도 되지만 Counter 사용
    cnt = Counter(clothes[1:n+1])
    
    # 0 이 없다면 모두 체육복이 있으므로 n리턴. 있다면 전체에서 0갯수만큼 뺀 숫자를 리턴
    if 0 not in cnt:
        return n
    else:
        return n - cnt[0]
        
        
        