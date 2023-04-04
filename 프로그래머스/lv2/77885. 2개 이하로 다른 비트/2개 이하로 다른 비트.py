def solution(numbers):
    answer = []
    
    for n in numbers:
        # 짝수면 이진수의 첫 자리면 1로 만들면 되므로 +1
        if n%2==0:
            answer.append(n+1)
        else:
            # 홀수일 때, 이진수 문자열의 맨 뒤부터 봐줘야하고
            # 문자열 내의 교체를 위해 리스트로 바꾼다. 따라서 맨 앞에 '0'을 더한 이진수 문자열을 뒤집어서 리스트화
            n2_li = list(bin(n)[2:][::-1]+'0')
            
            # 처음으로 0이 나오는 인덱스 저장
            i = n2_li.index('0')
            # 해당 인덱스는 1로 바꾸고, 그 이전의 인덱스는 0으로.
            # 실제로는 가장 작은 자릿수의 0을 1로 바꾸고, 그 이전의 수를 0,1 상관없이 0으로 바꿔주는 것
            n2_li[i],n2_li[i-1] = '1','0'
            # 다시 뒤집어서 n2로 저장하고 정답에 int함수를 써서 10진수로 저장
            n2 = ''.join(reversed(n2_li))            
            answer.append(int(n2,2))
    return answer