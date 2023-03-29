from collections import Counter
def solution(array):
    answer = 0
    for i in array:
        answer += Counter(str(i))['7']
    return answer