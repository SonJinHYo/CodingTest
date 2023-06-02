def solution(n, k, cmd):
    link = {}
    for i in range(n):
        link[i] = [i-1,i+1]
    answer = list('O'*n)
    stack = []
    
    
    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = link[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = link[k][0]

                
        elif c[0]=='C':
            prev,nxt = link[k]
            stack.append([prev,nxt,k])
            answer[k] ='X'

            
            if nxt==n:
                k = link[k][0]
            else:
                k = link[k][1]

                
            if prev == -1:
                link[nxt][0] = prev
            elif nxt==n:
                link[prev][1]=nxt
            else:
                link[prev][1] = nxt
                link[nxt][0] = prev

                
        else:
            prev,nxt,num = stack.pop()
            answer[num] = 'O'

            if prev == -1:
                link[nxt][0] = num
            elif nxt == n:
                link[prev][1] = num
            else:
                link[prev][1] = num
                link[nxt][0] = num


    return ''.join(answer)