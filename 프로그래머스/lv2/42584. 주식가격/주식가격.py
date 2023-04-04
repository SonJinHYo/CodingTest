from collections import deque

def solution(prices):
    # stack : (인덱스-1,주식 가격)을 쌓을 스택. 인덱스-1 인 이유는 처음 원소를 빼고 enumerate를 쓰기 때문
    # answer: 주식이 떨어지지 않은 기간을 저장할 리스트
    
    stack = [(-1,prices[0])]
    answer = [0 for _ in range(len(prices))]
    
    # 주식 가격을 순서대로 stack에 넣는다.
    for i,p in enumerate(prices[1:]):
        # 현재 가격이 마지막 주식 가격보다 떨어진다면
        while stack and stack[-1][1] > p:
            # 마지막 주식을 빼내면서 주식 인덱스에 기간을 저장
            idx,price = stack.pop()
            answer[idx+1] = i-idx
        # 현재 주식정보(인덱스,가격) 스택에 저장
        stack.append((i,p))
    #남아있는 주식은 전체기간-인덱스로 계산, 
    while(stack):
        idx,price = stack.pop()
        answer[idx+1] = len(prices)-2-idx
        
    return answer