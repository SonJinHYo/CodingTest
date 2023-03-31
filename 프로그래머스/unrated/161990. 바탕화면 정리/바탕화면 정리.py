def solution(wallpaper):
    r_min,r_max = 100,-1
    c_min,c_max = 100,-1
    for r,row in enumerate(wallpaper):
        for c,char in enumerate(row):
            if char == '#':
                r_min,r_max = min(r_min,r),max(r_max,r)
                c_min,c_max = min(c_min,c),max(c_max,c)
    return [r_min,c_min,r_max+1,c_max+1]