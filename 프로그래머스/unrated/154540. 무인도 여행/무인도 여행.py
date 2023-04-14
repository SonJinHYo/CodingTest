def solution(maps):
    answer = []
    rlim,clim = len(maps)-1,len(maps[0])-1
    move = {(1,0),(0,1),(-1,0),(0,-1)}
    global_visited = set()
    stack = [(0,0)]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (i,j) in global_visited:
                continue
            else:
                global_visited.add((i,j))
                stack = [(i,j)]
                visited = set()
                val = 0
                
                while stack:
                    r,c = stack.pop()
                    if maps[r][c]=='X' or (r,c) in visited:
                        continue
                    else:
                        visited.add((r,c))
                        global_visited.add((r,c))
                        val += int(maps[r][c])
                        for dr,dc in move:
                            new_r,new_c, = r+dr,c+dc
                            if not (0<=new_r<=rlim and 0<=new_c<=clim):
                                continue
                            else:
                                stack.append((new_r,new_c))
                if val != 0:
                    answer.append(val)

    return [-1] if not answer else sorted(answer)