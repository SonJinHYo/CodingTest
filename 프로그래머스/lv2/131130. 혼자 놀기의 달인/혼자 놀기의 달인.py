def solution(cards):
    try:
        grp = []
        visited = set()
        while len(visited)!=len(cards):
            start = (set(cards) - visited).pop()-1
            nxt = cards[start]
            tmp = [start+1]
            while start+1 != nxt:
                tmp.append(nxt)
                nxt = cards[nxt-1]
            grp.append(tmp)
            visited.update(tmp)
        grp.sort(key = lambda x: len(x),reverse=True)
        return len(grp[0])*len(grp[1])
    except:
        return 0