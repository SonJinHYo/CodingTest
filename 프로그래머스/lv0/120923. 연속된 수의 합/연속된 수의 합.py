def solution(num, total):
    mid = total//num if num%2==1 else total//num+1
    start = mid - num//2
    return [i for i in range(start,start+num)]
        
