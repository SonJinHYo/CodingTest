# p를 균형잡힌 u와 나머지 v로 나누는 함수
def div(p):
    cnt = 0
    for i,char in enumerate(p):
        cnt = cnt+1 if char=='(' else cnt-1
        if cnt == 0:
            return p[:i+1],p[i+1:]


# u가 올바른 괄호문자열인지 확인하는 함수
def check(u):
    cnt = 0
    for i,char in enumerate(u):
        cnt = cnt+1 if char=='(' else cnt-1
        if cnt<0:
            return False
        
    return True


def solution(p):
    if not p: # 1
        return ""
    
    u, v = div(p) # 2
    
    if check(u): # 3~3.1
        return u + solution(v)
    
    else: # 4
        answer = '('+solution(v)+')' # 4.1~4.3
        answer+=''.join('(' if c==')' else ')' for c in u[1:-1]) # 4.4
        return answer