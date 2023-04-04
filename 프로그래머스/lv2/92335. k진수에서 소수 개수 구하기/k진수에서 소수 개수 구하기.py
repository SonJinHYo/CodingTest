def conv(num,k):
    answer = ''
    while(num>0):
        answer+=str(num%k)
        num//=k
    return answer[::-1]

def check_p(n):
    if n == 1:
        return False
    i = 2
    while(i<=n**0.5):
        if n%i==0:
            return False
        i+=1
    return True

def solution(n, k):
    answer = 0
    s = conv(n,k)
    s_after = [int(i) for i in s.split(sep='0') if i.isdigit()]
    
    for i in s_after:
        if check_p(int(i)):
            answer+=1
    return answer