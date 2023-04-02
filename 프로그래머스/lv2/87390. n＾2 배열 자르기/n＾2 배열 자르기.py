def solution(n, left, right):
    # left와 rigth의 원래 행,열 위치를 저장
    L_row, L_col = left//n, left%n
    R_row, R_col = right//n, right%n
    
    answer = []
    # L행~R행 부분만 리스트로 만든다.
    # 리스트 원소값은 행값+1 보다 작으면 행값+1, 이후로는 1씩 커지는 리스트이다.
    for r in range(L_row,R_row+1):
        answer+=[i if i>(r+1) else (r+1) for i in range(1,n+1)]
    # L열,R열 값을 이용해 앞 뒤를 잘라서 반환.
    # 열만큼 앞뒤로 각각 잘라주면되고, (n-R_col) 이 0일수 있으므로 원소를 하나 추가해서 잘라준다.
    answer+=[0]
    return answer[L_col:-(n-R_col)]
    