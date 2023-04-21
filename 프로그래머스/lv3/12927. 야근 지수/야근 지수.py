from heapq import heappop,heappush,heapify

def solution(n, works):
    # 원소 부호를 반대로 work 리스트로 만들어주고
    work = [-i for i in works]
    # heapify로 리스트를 heap구조로 만들어준다
    heapify(work)
    
    # n번 빼야하므로 n번 반복
    for _ in range(n):
        # 첫 원소를 빼서 1을 더한걸 heappush로 넣어준다.
        heappush(work,heappop(work)+1)
        # 만약 가장 큰 원소가 양수라면(실제 음수)
        if work[-1]>0:
            # 0 반환
            return 0
        
    # 전체 원소의 제곱의 합을 반환
    return sum(i**2 for i in work)
