from itertools import combinations

# num이하의 소수 리스트를 반환하는 함수. 에라토스테네스의 체 활용
# 2이상부터 인덱스가 소수일 때 True, 아니면 False인 bool 리스트 리턴
def primeNumber(num):
    nums = int(num**0.5)
    number_list = [1 for i in range(num+1)]
    for i in range(2,nums+1):
        if number_list[i] == 0:
            continue
        else:
            for j in range(i+1,num+1):
                if j%i == 0:
                    number_list[j] = 0
    return number_list
                    
    
def solution(nums):
    answer = 0
    # nums 리스트를 정렬해서 마지막 세 수를 더한 값이 최대. 최댓값 이하의 소수리스트를 생성
    nums.sort()
    prime_list = primeNumber(nums[-1]+nums[-2]+nums[-3])
    
    # nums 리스트의 세 숫자를 조합으로 탐색
    for li in combinations(nums,3):
        # 세 숫자의 합이 소수면 answer+1. (li = 고른 세 숫자 튜플)
        if prime_list[sum(li)]==1:
            answer+=1
            
    return answer