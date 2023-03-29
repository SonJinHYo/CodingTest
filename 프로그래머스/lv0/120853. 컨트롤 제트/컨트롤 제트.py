def solution(s):
    tmp = []
    for c in s.split():
        print(c)
        if c=='Z' and tmp:
            tmp.pop()
        elif c!='Z':
            tmp.append(int(c))
    return sum(tmp)