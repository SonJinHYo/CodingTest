def solution(s):
    answer = True
    
    pn = 0
    yn = 0
    s = s.lower()
    print(s)
    for i in s:
        if i=='p':
            pn+=1
        elif i=='y':
            yn+=1
    if(pn==yn):
        return True
    else:
        return False

    