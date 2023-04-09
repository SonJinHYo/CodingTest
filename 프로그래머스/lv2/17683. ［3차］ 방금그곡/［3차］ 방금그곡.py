def rep(s):
    # '#'음정이 있는 음을 한 문자로 줄이기
    d = {'C#':'c','D#':'d','F#':'f','G#':'g','A#':'a'}
    # 딕셔너리를 돌며 모든 #문자를 축소
    for k,v in d.items():
        s = s.replace(k,v)
    return s

def solution(m, musicinfos):
    # 주어진 m 치환
    m = rep(m)
    # 제목 , 재생시간을 저장할 튜플
    answer = ('',0)
    for musicinfo in musicinfos:
        # 음악 시작, 끝, 제목, 음 으로 나눈다.
        s,e,title,music = musicinfo.split(',')
        # 재생시간을 구해준다
        run_time = int(e[:2])*60+int(e[3:]) - int(s[:2])*60 - int(s[3:])
        # 음에서 '#'음정 치환
        music = rep(music)
        
        # 음악 길이가 재생시간보다 길어질 때 까지 늘려준 다음 재생시간만큼 자른다.
        while len(music)<=run_time:
            music*=2
        music = music[:run_time]
        # 음악 안에 찾는 멜로디 m이 없으면 넘어가고, 있으면 재생시간이 큰 쪽을 answer에 저장
        if music.find(m)==-1:
            continue
        else:
            answer = (title,run_time) if answer[1] < run_time else answer
    # answer의 첫 원소가 초기화상태 그대로면, 없을 시 문구 리턴
    if answer[0] =='':
        return '(None)'
    
    # 있다면 title 리턴
    return answer[0]