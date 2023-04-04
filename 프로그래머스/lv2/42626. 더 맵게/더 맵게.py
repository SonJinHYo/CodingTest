from heapq import heapify,heappush,heappop

def solution(scoville, K):
    answer = 0
    # scoville 리스트를 힙구조화 한다.
    heapify(scoville)
    while(scoville[0]<K):
        # 모든 스코빌 조합을 다 써서 하나만 남아도 K보다 작다면 -1
        if len(scoville)<2:
            return -1
        
        # 힙을 통해 가장 작은 두 값을 꺼내어 계산 후 힙에 넣는다
        scov1 = heappop(scoville)
        scov2 = heappop(scoville)
        heappush(scoville,scov1+scov2*2)
        answer+=1
        
    
    return answer









