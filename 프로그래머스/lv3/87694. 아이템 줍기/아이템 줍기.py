from collections import deque

# def move(board,pos):
#     x,y = pos
#     def check(x1,y1):
#         if board[y1][x1]!=1:
#             return False
#         else:
#             for i in range(x1-1,x1+2):
#                 for j in range(y1-1,y1+2):
#                     if board[j][i] == 0:
#                         return True
#         return False
#     re = []
#     if check(x+1,y):
#         re.append((x+1,y))
#     if check(x,y+1):
#         re.append((x,y+1))
#     if check(x-1,y):
#         re.append((x-1,y))
#     if check(x,y-1):
#         re.append((x,y-1))
        
#     return re

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    board = [[0]*153 for _ in range(153)]
    for rec in rectangle:
        x1,y1,x2,y2 = rec
        x1,y1,x2,y2 = x1*3,y1*3,x2*3,y2*3
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                board[y][x] = 1
                
                
    def move(pos):
        x,y = pos
        
        def check(x1,y1):
            if board[y1][x1]!=1:
                return False
            else:
                for i in range(x1-1,x1+2):
                    for j in range(y1-1,y1+2):
                        if board[j][i] == 0:
                            return True
            return False
        
        re = []
        if check(x+1,y):
            re.append((x+1,y))
        if check(x,y+1):
            re.append((x,y+1))
        if check(x-1,y):
            re.append((x-1,y))
        if check(x,y-1):
            re.append((x,y-1))

        return re
    
    
    
    
    q = deque([(characterX*3,characterY*3,0)])
    visited = set()
    while(q):
    # for _ in range(1):
        x,y,ans = q.popleft()
        
        if (x,y) == (itemX*3,itemY*3):
            return ans//3
        else:        
            if (x,y) not in visited:
                visited.add((x,y))
                for i in move((x,y)):
                    if i not in visited:
                        q.append((i[0],i[1],ans+1))
