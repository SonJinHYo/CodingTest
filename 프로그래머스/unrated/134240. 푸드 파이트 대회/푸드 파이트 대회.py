def solution(food):
    left_food = [i//2 for i in food[1:]]
    answer = ''
    for i,k in enumerate(left_food):
        answer += str(i+1)*k
    answer += '0' + answer[::-1]
    return answer