def solution(A,B):
    answer = 0
    # 주어진 수의 합이 정해진 경우, 두 수의 차가 클수록 곱이 커진다 (산술기하평균 참고)
    # 두 리스트를 각각 내림차순,오름차순 정렬하여 순서대로 곱해주면 최소가 나온다
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]

    return answer