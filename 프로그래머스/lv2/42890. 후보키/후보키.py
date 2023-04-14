from itertools import combinations

def solution(relation):
    # R,C : 행,열 길이
    R = len(relation)
    C = len(relation[0])
    # 후보키로 사용한 조합을 저장할 집합
    index_used = set()
    answer = 0
    # 후보키 리스트
    col_li = [i for i in range(C)]
    
    # 후보키 중 1~n개까지 조합으로 뽑는다
    for n in range(1,C+1):
        # col_idx : 식별할 후보키
        for col_idx in combinations(col_li,n):
            # 이미 사용한 조합이 포함되어 있다면 넘어간다.
            flag = False
            for idx_li in index_used:
                if set(idx_li)<set(col_idx):
                    flag= True
            if flag:
                continue
            
            # 후보키로 모든 사람을 집합 tmp에 넣는다
            tmp = set()
            for r in range(R):
                tmp.add(tuple([relation[r][c] for c in col_idx]))
            # 다 넣어도 모든 사람 수(R) 과 크기가 같다면, 겹치는 것이 없었다는 뜻이므로
            if len(tmp)==R:
                # answer을 +1해주고 후보키에 넣는다
                answer+=1
                index_used.add(col_idx)
    
    return answer
