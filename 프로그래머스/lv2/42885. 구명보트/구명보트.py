from heapq import heappop,heapify

def solution(people, limit):
    answer = 0
    # 무게순으로 정렬
    people.sort()
    # 가벼운사람 인덱스, 무거운 사람 인덱스
    front,end = 0, len(people)-1
    while(front<=end):
        # 맨 앞, 맨 뒤 사람의 무게 합이 한계치 이하라면 맨 앞 사람도 타고(인덱스+1)
        if(people[front]+people[end]<=limit):
            front+=1
        # 뒷 사람도 탄다 (인덱스-1)
        end-=1
        # 왕복 횟수+1
        answer+=1
                
    return answer