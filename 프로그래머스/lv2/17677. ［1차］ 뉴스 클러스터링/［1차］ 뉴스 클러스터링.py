from collections import deque

def solution(str1, str2):
    
    # 문자열의 다중 집합을 만드는 함수
    def make_li(str1):
        c1 = []
        
        for i in range(len(str1)):
            # 두 문자를 끊어서
            check_str = str1[i:i+2]
            # 문자가 한 개 남은 상황같이 갯수가 부족하다면 넘어간다.
            if len(check_str) < 2:
                continue
            # 두 문자가 모두 알파벳이라면 append로 저장
            if all(c.isalpha() for c in check_str):
                c1.append(check_str)
        return c1
    # c1,c2 : 두 문자의 다중집합
    # n1,n2 : 두 다중집합의 길이. 합집합 크기를 구할 때 사용
    c1 = make_li(str1.lower())
    c2 = make_li(str2.lower())
    n1,n2 = len(c1),len(c2)
    # cnt : 교집합 갯수
    cnt = 0
    while(c1):
        check = c1.pop()
        # check가 다른 다중집합에도 있다면
        if check in c2:
            # 겹치는 원소를 제거하며 교집합갯수+1
            c2.remove(check)
            cnt+=1
            
    # 만약 둘 중 하나가 공집합과 같은 분모가 0이 되는 상황이라면 65536 리턴            
    if (n1+n2-cnt)==0:
        return 65536
    # 아니라면 (자카드 유사도)*65536 리턴
    else:
        return int(cnt/(n1+n2-cnt)*65536)