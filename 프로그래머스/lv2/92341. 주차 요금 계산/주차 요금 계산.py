from math import ceil
from collections import defaultdict

def solution(fees, records):
    # time_dict (dict) : 키,값 == 차량번호 , 주차장 이용 시간
    # parking (set) : 주차장
    # parking_dict (dict) : 주차한 차량 주차 시작시간
    # fee_list (list) : (차량,주차요금) 튜플을 저장할 리스트
    time_dict = defaultdict(int)
    parking = set()
    parking_dict = {}
    fee_list = []
    
    for info in records:
        # records의 원소를 split해서 따로 저장한다. time은 분단위로 바꿔 계산해준다
        time,car_num,check = info.split()
        time = 60*int(time[:2])+int(time[3:])
        
        # 차량이 들어왔다면 주차장에 추가하고 주차시작 시간을 저장
        if check=='IN':
            parking.add(car_num)
            parking_dict[car_num] = time
            
        # 나간다면 주차장에서 빼고, 주차한 시간을 time_dict에 저장
        else:
            parking.remove(car_num)
            time_dict[car_num]+=(time - parking_dict[car_num])
    
    # 아직 주차장에 남은 차량들을 빼내면서 23:59분(1439분)에 나간걸로 계산
    while(parking):
        car_num = parking.pop()
        time_dict[car_num]+=(1439 - parking_dict[car_num])
        
    # time_dict에서 조건에 맞게 주차요금을 계산하여,
    for car_num,t in time_dict.items():
        if t<=fees[0]:
            fee = fees[1]
        else:
            fee = fees[1]+ceil((t-fees[0])/fees[2])*fees[3]
        # (차량번호,요금) 을 fee_list에 저장
        fee_list.append((car_num,fee))
    
    # 차량번호 기준으로 정렬한 리스트의 두번째 원소(요금)만 리턴
    return [i[1] for i in sorted(fee_list,key=lambda x: x[0])]