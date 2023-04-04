from collections import deque

def solution(bridge_length, weight, truck_weights):
#     # 남는 다리길이가 1 이상인지, 현재 트럭의 무게가 남는 무게치를 안넘는지 확인.
#     # 넣을 수 있는 트럭을 넣은 후, 길이를 하나 줄이고, 남는 무게치도 트럭무게만큼 줄인다
#     # 트럭은다리 리스트에 넣는다. 넣을 때는 [무게,다리길이] 를 넣는다
#     # 위 과정이 끝나면
#     # 다리 리스트를 돌면서 원소들의 다리 길이를 1씩 뺀다
#     # 다리 리스트의 마지막 원소의 다리 길이를 확인한다. 0이면 빼고 남는 무게에 트럭무게를 더한다
#     # 트럭리스트,다리 리스트가 다 0이 될때까지 반복한다
#     # 한 반복문 당 answer을 1씩 더한다
    answer = 0
    in_bridge = []
    remain_w = weight

    while(truck_weights or in_bridge):
        if truck_weights and remain_w >= truck_weights[0]:
            in_bridge.append([truck_weights[0],bridge_length])
            remain_w-=truck_weights[0]
            truck_weights.pop(0)

        for i in range(len(in_bridge)):
            in_bridge[i][1]-=1
        
        if in_bridge and in_bridge[0][1]==0:
            remain_w += in_bridge[0][0]
            in_bridge.pop(0)
        answer+=1
        
    return answer+1