def solution(s):
    l = len(s)
    if l==1:
        return 1
    answer = []
    
    for n in range(1,(l//2)+1):
        ss = ''
        cnt = 1
        for i in range(0,l,n):

            if s[i:i+n] == s[i+n:i+2*n]:
                cnt+=1
                
            else:
                if cnt==1:
                    ss+=s[i:i+n]
                else:
                    ss+=(str(cnt)+s[i-n:i])
                    cnt=1
        answer.append(len(ss))
        
    return min(answer)












