def check(num):
    if not num.isdigit():
        return False
    for i in range(1,5):
        if num != num.replace(str(i)*2,str(i)):
            return False
    return True

def solution(babbling):
    dic = {'aya':'1','ye':'2','woo':'3','ma':'4'}
    answer = 0
    for s in babbling:
        for k,v in dic.items():
            s = s.replace(k,v)
        
        if check(s):
            answer+=1
    return answer