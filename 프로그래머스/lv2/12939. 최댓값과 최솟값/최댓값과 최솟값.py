def solution(s):
    # 문자열을 잘라내서 정렬된 정수리스트로 바꿔준다
    arr = sorted(map(int,s.split()))
    # 처음과 마지막 값을 join함수로 빈칸으로 붙여서 리턴한다
    return ' '.join(map(str,[arr[0],arr[-1]]))