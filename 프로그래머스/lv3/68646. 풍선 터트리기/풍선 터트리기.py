from heapq import heappush,heappop,heapify

def solution(a):
    if len(a)<= 3:
        return len(a)
    
    answer = 2
    left_heap,left_min = [a[0]],[a[0]]
    right_heap,right_min = [a[-1]],[a[-1]]
    
    for i in range(1,len(a)-1):
        heappush(left_heap,a[i])
        left_min.append(left_heap[0])
        
        heappush(right_heap,a[-i-1])
        right_min.append(right_heap[0])
    right_min = [i for i in reversed(right_min)]
    
    for i in range(1,len(a)-1):
        if not (left_min[i]<a[i] and right_min[i]<a[i]):
            answer+=1
            
    return answer