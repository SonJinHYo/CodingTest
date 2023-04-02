def solution(n):
    # 1이라면 한 칸 뿐이므로 1 리턴
    if n == 1:
        return 1
    # 처음 두 경우의수 초기화
    arr = [1,2]
    
    while(len(arr)<n):
        # 다음 계단에 도착하는 경우 = 이전 계단에서 한칸 + 전전 계단에서 두 칸
        # 따라서 이전 경우의 수+ 전전 경우의 수
        arr.append((arr[-1]+arr[-2])%1234567)
        
    return arr[-1]