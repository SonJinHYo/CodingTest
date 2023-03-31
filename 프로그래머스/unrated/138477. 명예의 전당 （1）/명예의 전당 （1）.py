from heapq import heappop, heappush, heapify

def solution(k, score):
    answer = [min(score[:i]) for i in range(1,k+1)]
    heap = [i for i in score[:k]]
    
    if k>len(score):
        return answer[:len(score)]
    
    heapify(heap)
    for s in score[k:]:
        # print(heap)
        heappush(heap,s)
        heappop(heap)
        answer.append(heap[0])
    
    return answer