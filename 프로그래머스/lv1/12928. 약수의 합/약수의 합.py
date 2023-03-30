def solution(n):
    if n==0:
        return 0
    if n==1:
        return 1
    i = 2
    j = 0
    arr = []
    answer = 1
    while(n>1):
        if n%i==0:
            j+=1
            if(n==i):
                arr.append([i,j])
                break
            n/=i
        else:
            arr.append([i,j])
            i+=1
            j=0
    for i in arr:
        if(i[1]==0):
            continue
        answer *= (i[0]**(i[1]+1)-1)/(i[0]-1)
    print(arr)
    return answer