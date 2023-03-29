def solution(sides):
    sides.sort()
    L1 = len([i for i in range(1,sides[1]) if i+sides[0]>sides[1]])
    L2 = len([i for i in range(sides[1],sides[0]+sides[1])])
    return L1+L2