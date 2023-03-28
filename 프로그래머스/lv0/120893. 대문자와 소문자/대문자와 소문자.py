def solution(my_string):
    return ''.join([i.lower() if ord(i)<ord('a') else i.upper() for i in my_string ])