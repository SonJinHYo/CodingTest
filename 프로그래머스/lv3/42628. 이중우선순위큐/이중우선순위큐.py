import heapq as hp

def solution(operations):
    h = []
    for i in operations:
        op,num = i.split()
        if op == 'I':
            hp.heappush(h,int(num))
        else:
            if not h:
                continue
            else:
                if num=='1':
                    h.pop()
                else:
                    hp.heappop(h)
    if not h:
        return [0,0]
    return [max(h),min(h)]