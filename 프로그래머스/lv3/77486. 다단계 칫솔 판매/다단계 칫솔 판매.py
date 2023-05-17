from math import floor

def solution(enroll, referral, seller, amount):
    # 추천인관계를 딕셔너리로 키,값 = 추천인, 추천받은사람
    rec_map = {}
    money_map ={'center':0}
    for i in range(len(enroll)):
        if referral[i] == '-':
            rec_map[enroll[i]] = 'center'
        else:
            rec_map[enroll[i]] = referral[i]
        money_map[enroll[i]] = 0
            
    for i in range(len(amount)):
        amount[i]*=100
    
    for i in range(len(seller)):
        money = amount[i]
        s = seller[i]
        while(money>0):
            r_money = floor(money*0.1)
            money_map[s] += (money - r_money)
            money = r_money
            if s in rec_map:
                s = rec_map[s]
            else:
                break
    answer = []
    for name in enroll:
        answer.append(money_map[name])
        
    return answer