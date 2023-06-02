# def calculate_n(X, Y):
#     n_set = set()
#     for x in X:
#         for y in Y:
#             n_set.add(x+y)
#             n_set.add(x-y)
#             n_set.add(x*y)
#             if y != 0:
#                 n_set.add(x//y)
#     return n_set

# def solution(N, number):
#     answer = -1
#     result = {}   # key는 숫자 사용횟수, value는 숫자를 key번 사용했을 때 나오는 연산 결과셋
#     result[1] = {N} # N을 1번 사용할 때는 그냥 N
#     if number == N:
#         return 1
#     for n in range(2, 9):  # 8번까지만 계산하므로
#         i = 1
#         temp_set = {int(str(N)*n)}  # N=5, 2번 사용할 때 먼저 55를 저장
#         # 1 (op) N-1.... n-1 (op) 1 까지 계산
#         while i < n:
#             temp_set.update(calculate_n(result[i], result[n-i]))
#             i += 1
#         # 만들어진 셋에 원하는 숫자가 있으면 stop
#         if number in temp_set:
#             answer = n
#             break

#         result[n] = temp_set

#     return answer

def nxt_num(A,B):
    result = set()
    for a in A:
        for b in B:
            result.update({a+b,a-b,a*b})
            if b!=0:
                result.add(a//b)
    return result
    

def solution(N, number):
    if number==N:
        return 1
    
    cnt_dict = {1:{N},2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
    for k in range(2,9):
        i = 1
        cnt_dict[k].add(int(str(N)*k))

        while(i<k):
            cnt_dict[k].update(nxt_num(cnt_dict[i],cnt_dict[k-i]))
            i+=1
        
        if number in cnt_dict[k]:
            return k
        
    return -1
        
