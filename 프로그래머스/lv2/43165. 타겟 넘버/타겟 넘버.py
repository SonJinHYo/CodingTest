from itertools import product

def solution(numbers, target):
    L = len(numbers)
    # answer : 타겟 넘버가 나온 횟수
    answer = 0
    # 'True,False를 중복순열로 L번 뽑은 결과' 를 반복문으로 돈다. 
    # ex. prod = [T,T,T,F,F] / [F,F,T,F,T] 와 같은 꼴
    for prod in product([True,False],repeat = L):
        ans = 0
        # prod[i]==True라면 number[i]를 더하고 아니라면 뺀다.
        for i in range(L):
            if prod[i]:
                ans+=numbers[i]
            else:
                ans-=numbers[i]
        # 계산 결과가 타겟넘버라면 answer+1
        if ans==target:
            answer+=1
    return answer