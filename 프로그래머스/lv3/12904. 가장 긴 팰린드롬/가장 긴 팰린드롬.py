def solution(s):
    if len(s) <= 2:
        if len(s)==2 and s[0]==s[1]:
            return 2
        return 1
    
    answer = 0
    for idx in range(1,len(s)-1):
        palin_even,palin_odd = 0,0
        while (idx+palin_even != len(s) and idx-1-palin_even != -1) and (s[idx-1-palin_even] == s[idx+palin_even]):
            palin_even+=1

        while (idx+palin_odd != len(s) and idx-palin_odd != -1) and (s[idx+palin_odd] == s[idx-palin_odd]):
            palin_odd+=1
            
        answer = max(answer,palin_even*2,palin_odd*2-1)
    return answer