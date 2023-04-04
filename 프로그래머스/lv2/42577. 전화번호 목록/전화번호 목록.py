def solution(phone_book):
    # 전화번호부를 문자, 길이 순으로 정렬한다.
    new_book = sorted(phone_book,key=lambda x: [x,len(x)])
    for i in range(len(new_book)-1):
        # 현 전화번호 == 다음 전화번호부(현 전화번호부 길이까지) 와 같다면 False
        if new_book[i]==new_book[i+1][:len(new_book[i])]:
            return False
    # 같은적이 없었다면 True
    return True
