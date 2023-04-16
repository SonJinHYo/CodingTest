from heapq import heappush,heappop

def solution(plans):
    answer,heap,tmp = [],[],[]
    for a,b,c in plans:
        heappush(heap,(int(b[:2])*60+int(b[3:]),int(c),a))

    while heap:
        start,rem,sbj = heappop(heap)
        gap = heap[0][0]-(start+rem) if heap else 1e9
        if gap < 0:
            tmp.append((start+rem-heap[0][0],sbj))
            
        else:
            answer.append(sbj)
            
            while tmp and gap>0:
                tmp_rem,tmp_sbj = tmp.pop()
                if gap-tmp_rem < 0:
                    tmp.append((tmp_rem-gap,tmp_sbj))
                    gap=0
                else:
                    gap-=tmp_rem
                    answer.append(tmp_sbj)
        
    return answer