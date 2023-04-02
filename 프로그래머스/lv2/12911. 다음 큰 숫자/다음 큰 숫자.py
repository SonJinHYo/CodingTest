from collections import Counter

def solution(n):
    
    # 현재 이진수의 1갯수를 k에 저장
    k = Counter(bin(n)[2:])['1']
    
    # 1의 갯수가 같아질때까지 n을 증가시키면서 같아지면 n값 리턴
    while(n<1000000):
        n+=1
        if k == Counter(bin(n)[2:])['1']:
            return n
        
    