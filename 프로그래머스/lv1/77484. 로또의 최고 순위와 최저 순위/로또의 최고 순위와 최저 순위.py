def solution(lottos, win_nums):
    # 원소를 가지고 있는지 판단할 때, 리스트보다 집합이 빠르다.
    w = set(win_nums)
    # ans = [맞은 갯수 최대,맞은 갯수 최소]
    ans = [0,0]
    while lottos:
        # 로또 숫자를 하나 꺼내서 n에 저장
        n = lottos.pop()
        # 0 이라면 최대 +1
        if n==0:
            ans[0]+=1
        # 당첨숫자에 포함된다면 최대,최소 둘 다 +1
        elif n in w:
            ans[0]+=1
            ans[1]+=1
    # 7-맞은갯수 리턴, 단 i==0일 땐 낙첨이므로 6을 리턴            
    return [7-i if i!=0 else 6 for i in ans]