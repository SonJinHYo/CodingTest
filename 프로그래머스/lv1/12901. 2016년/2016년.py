def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    start_index = 4
    date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    for i in range(1,a):
        start_index = (start_index+month[i-1])%7
        
    return date[(start_index+b-1)%7]