from collections import deque

def solution(cacheSize, cities):
    # cacheSize가 0이면 매번 가져올게 없으므로 모든 시간이 5초
    if cacheSize==0:
        return 5*len(cities)
    
    # answer : 반환값
    # c : 도시를 저장할 deque
    # q : 모든 도시를 소문자로 저장해놓은 deque
    answer = 0
    c = deque()
    q = deque([s.lower() for s in cities])
    
    # q가 빌 때 까지 뺀다
    while(q):
        # 빼낼 도시가 c안에 있다면 실행시간 1초
        if q[0] in c:
            answer+=1
            # 해당 도시를 삭제
            del c[c.index(q[0])]
        # c안에 도시가 없고 아직 공간에 여유가 있다면 실행시간 +5초
        elif len(c)<cacheSize:
            answer+=5
        # c안에 도시가 없고 공간에 여유도 없다면 맨 앞 원소를 뺀 뒤 +5초
        else:
            answer+=5
            c.popleft()
        # q에서 뺀 도시를 c에 추가
        c.append(q.popleft())
    return answer