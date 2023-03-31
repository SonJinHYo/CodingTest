def solution(s):
    answer = 0
    me,another,my_char = 0,0,None
    for idx,c in enumerate(s):
        if not my_char:
            my_char,me = c,1
        else:        
            me = me+1 if my_char==c else me
            another = another+1 if my_char!=c else another
            
        if idx==(len(s)-1) or me==another:
            me,another,my_char = 0,0,None
            answer+=1
        
    return answer