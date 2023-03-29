def solution(array, n):
    arr = {i:abs(n-i) for i in array}
    return sorted(arr.items(),key=lambda x: [x[1],x[0]])[0][0]