def solution(n):
    answer = ''
    # 3진법으로 바꿔주기. 단, 뒤집힌 3진법이 나오게 된다.
    while(n>0):
        answer += str(n%3)
        n//=3
    # 뒤집혀져 있는 3진법을 int함수를 이용하여 10진법으로 바꿔준다    
    return int(answer,3)