from itertools import permutations

def make_prime_table(n):
    # n까지의 소수의 집합을 리턴한다.
    # 에라토스테네스의 체 방법을 사용.
    arr = [True for _ in range(n)]
    prime_set = set()
    for i in range(2,n):
        if arr[i] == True:
            prime_set.add(i)
            for j in range(i,n,i):
                arr[j] = False
        else:
            continue
    return prime_set

def solution(numbers):
    # numbers의 자릿수까지만 소수를 집합으로 생성
    prime_set = make_prime_table(10**len(numbers))
    
    # 정답 집합. 같은 숫자가 등장할 경우 같은 소수가 나와서 들어갈 수 있다. 따라서 집합으로 정의
    answer = set()
    
    # numbers의 자릿수들을 순열로 체크한다. k는 자릿수
    for k in range(1,len(numbers)+1):
        
        # numbers의 숫자를 k 자릿수만큼 순열로 확인
        for num_li in permutations(list(numbers),k):
            
            # 자릿수들을 정수로 바꾼 결과가 소수집합 안에 있다면 정답 집합에 추가
            num = int(''.join(num_li))
            if num in prime_set:
                answer.add(num)
                
    # 소수 갯수를 리턴
    return len(answer)