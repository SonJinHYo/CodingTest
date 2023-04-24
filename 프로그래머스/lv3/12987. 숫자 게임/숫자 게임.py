from heapq import heapify,heappop,heappush
def solution(A, B):
    answer = 0
    heapify(A)
    heapify(B)
    while(B):
        if A[0]<B[0]:
            answer+=1
            heappop(A)
            heappop(B)
        else:
            heappop(B)
        
    
    return answer