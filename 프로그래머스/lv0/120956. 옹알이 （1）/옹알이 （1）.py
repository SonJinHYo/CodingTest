from itertools import permutations

def solution(babbling):
    answer = 0
    label = {'aya':'1','ye':'2','woo':'3','ma':'4'}
    for i in range(n:=len(babbling)):
        for k,v in label.items():
            babbling[i] = babbling[i].replace(k,v)
            
    for s in babbling:
        if s.isdigit() and not set(i for i in range(1,len(s)) if s[i-1]==s[i]):
            answer+=1
        
    return answer