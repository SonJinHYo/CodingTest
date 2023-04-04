def solution(dirs):
    move = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    pos = [0,0]
    maps = set()
    for d in dirs:
        # 경계를 넘는다면 위치 유지, 그렇지 않다면 이동한 위치로 반환
        new_x,new_y = [pos[i]+move[d][i] \
                       if pos[i]+move[d][i] not in {6,-6} else pos[i] for i in range(2)]
        # 위치가 바뀌었다면 간선 저장, 위치 이동
        if [new_x,new_y]!=pos:
            maps.add(((pos[0],pos[1]),(new_x,new_y)))
            maps.add(((new_x,new_y),(pos[0],pos[1])))
            pos = [new_x,new_y]
        
    return len(maps)//2