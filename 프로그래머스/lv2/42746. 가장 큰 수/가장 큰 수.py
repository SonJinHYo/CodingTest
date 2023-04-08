def solution(numbers):
    # 순서대로 풀어쓰면
    # 문자열로(리스트를 정수로(numbers의 숫자를 문자열로 정렬), 문자열*3을 해준 것을 반대로 정렬)
    # 문자열 *3 을 해주는 이유는? 1000 이하 숫자가 오므로 자릿수 관계없이 앞부터 큰 숫자가 와야한다.
    # 문자열 길이를 3배 해주면 자릿수에 관계없이 숫자로만 정렬이 된다
    return str(int(''.join(sorted(list(map(str,numbers)),key = lambda x: str(x)*3,reverse=True))))
