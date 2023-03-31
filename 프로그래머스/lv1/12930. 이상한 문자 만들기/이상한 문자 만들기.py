def solution(s):
    answer,cnt= [],0
    
    for c in s:
        if c==' ':
            answer.append(c)
            cnt=0
            
        else:
            new_c = c.upper() if cnt%2==0 else c.lower()
            cnt+=1
            answer.append(new_c)
            
    return ''.join(answer)