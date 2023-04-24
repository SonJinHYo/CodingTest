def solution(routes):
    answer = 0
    """
    차량 경로를 시작순으로 오름차순 정렬
    첫 차량의 경로 끝을 end로 설정
    이후 루트를 순차로 돌면서 
    경로의 시작이 end이상이면
    answer+1을 해주고 이 차량의 끝을 다시 end로 설정
    경로의 시작이 end 이하면
    경로의 끝이 end보다
    """
    routes.sort(key=lambda x:x[1])
    end = -30001
    for route in routes:
        s,e = route
        if s > end:
            end = e
            answer+=1
    
    return answer