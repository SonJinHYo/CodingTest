from itertools import product

def solution(word):
    d = {'A':1,'E':2,'I':3,'O':4,'U':5}
    answer = 0
    for i,char in enumerate(word):
        answer+= (d[char]-1)*(5**(5-i)-1)//4+1
    
    return answer