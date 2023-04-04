def solution(record):
    # comments (dict): 입력에 따른 출력멘트를 저장
    # d (dict) : key,value == 유저uid, 닉네임
    # answer (list) : 정답멘트 저장
    comments = {'Enter':'들어왔습니다.','Leave':'나갔습니다.'}
    d = {}
    answer = []
    
    # 닉네임 결과를 먼저 정리한다
    for info in record:
        info = info.split()
        # Leave가 아니라면 유저의 uid,닉네임을 딕셔너리에 저장
        if info[0]!='Leave':
            d[info[1]] = info[2]
            
    # 정리된 닉네임으로 출력문자열 저장
    for info in record:
        info = info.split()
        # Change는 필요 없으므로 제외.
        if info[0]!='Change':
            answer.append(f'{d[info[1]]}님이 {comments[info[0]]}')
            
    return answer