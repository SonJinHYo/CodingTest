from math import ceil

def solution(n, stations, w):
    answer = 0
    empty_len_li = [stations[0]-w-1]
    cover_len = w*2+1
    for i in range(1,len(stations)):
        empty_len_li.append(stations[i]-stations[i-1]-2*w-1)
    empty_len_li.append(n-stations[-1]-w)
    for L in empty_len_li:
        if L>0:
            answer += ceil(L/cover_len)

    return answer