def solution(s, skip, index):
    answer = ''
    skip = {ord(i) for i in skip}
    for c in s:
        new_c = ord(c)
        for _ in range(index):
            new_c = new_c +1 if new_c < ord('z') else ord('a')
            while new_c in skip:
                new_c = new_c +1 if new_c < ord('z') else ord('a')
        answer += chr(new_c)
    return answer