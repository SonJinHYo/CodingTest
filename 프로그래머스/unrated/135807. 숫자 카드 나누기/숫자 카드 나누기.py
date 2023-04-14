from math import gcd

# 리스트 내의 숫자들의 최대공약수를 구하는 함수
def array_gcd(num_list):
    result = num_list[0]
    for n in num_list[1:]:
        result = gcd(result,n)
    return result


def solution(arrayA, arrayB):
    # A,B 최대공약수
    A_gcd,B_gcd = array_gcd(arrayA),array_gcd(arrayB)
    
    for i in range(len(arrayA)):
        A_gcd = 1 if arrayB[i]%A_gcd == 0 else A_gcd
        B_gcd = 1 if arrayA[i]%B_gcd == 0 else B_gcd
        
    return max(A_gcd,B_gcd) if not (A_gcd==1 and B_gcd==1) else 0