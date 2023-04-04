from collections import deque

def solution(files):
    answer = []
    for file in files:
        # 파일명을 deque로 만들고
        file = deque(file)
        head,num= '',''
        
        # 숫자가 나올때까지 deque에서 빼며 head에 더한다
        while not file[0].isdigit():
            head+=file.popleft()
        # file이 남아있고, 길이는 5미만, 다음 문자가 숫자면, deque에서 빼며 head에 더한다
        while file and len(num)<5 and file[0].isdigit():
            num+=file.popleft()
        # 남은건 전부 빼서 tail에 더한다.
        tail =''.join(list(file))
        
        answer.append((head,num,tail))
    answer.sort(key = lambda x: [x[0].lower(),int(x[1])])
    return [''.join(li) for li in answer]