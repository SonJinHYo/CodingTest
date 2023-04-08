def conv(n):
    d = {0:'4',1:'1',2:'2'}
    answer = ''
    while(n>0):
        answer +=d[n%3]
        if n%3==0:
            n//=3
            n-=1
        else:
            n//=3
    return answer[::-1]

def solution(n):
    d = {0:'4',1:'1',2:'2'}
    answer = ''
    while(n>0):
        answer +=d[n%3]
        if n%3==0:
            n//=3
            n-=1
        else:
            n//=3
    return answer[::-1]
