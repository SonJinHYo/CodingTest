import numpy as np
from collections import Counter
    
def DownBlock(m,n,board):
    for c in range(n):
        # c 열의 알파벳만 new_c에 추가 (사라져야할 '0' 제외)
        new_c = [char for char in board[:,c] if char.isalpha()]
        # 열 갯수를 모자란만큼 '1'로 채움
        new_c =['1']*(m-len(new_c)) + new_c
        # new_c를 새로운 열로 저장
        board[:,c] = np.array(new_c)
        
def solution(m, n, board):
    # 넘파이 문자 Array를 만든다.
    board = np.array([list(i) for i in board])
    
    while(True):
        save_index = []
        # 배열을 2x2 사이즈로 돌면서, 2x2내 모든 원소가 '1'이 아닌 것으로 같으면
        # ('1'은 사라진 빈칸블록)
        for r in range(m-1):
            for c in range(n-1):
                if board[r,c]!='1' and np.all(board[r:r+2,c:c+2]==board[r,c]):
                    # 그 때 인덱스 저장
                    save_index.append((r,c))
        # 저장된 인덱스가 없으면 (사라진 블록이 없으면) 반복 종료
        if not save_index:
            break
        
        # 사라질 블록은 0으로 채워준 다음
        for r,c in save_index:
            board[r:r+2,c:c+2].fill(0)
        # 블록들을 내려준다.
        DownBlock(m,n,board)

    # k : 남은 원소
    # v : 남은 원소들 갯수
    k,v = np.unique(board,return_counts=True)
    # 딕셔너리로 만들어서 '1'이 없으면(사라진 블록이 없으면) 0 리턴
    ans = dict(zip(k,v))
    if '1' not in ans:
        return 0
    # 있다면 1의 갯수 반환
    return int(ans['1'])