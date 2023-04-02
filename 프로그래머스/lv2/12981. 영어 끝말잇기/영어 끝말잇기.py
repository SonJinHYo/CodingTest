def solution(n, words):
    # 사용한 단어 집합
    used_words = {words[0]}
    # 직전 단어. 첫 단어로 초기화
    w = words[0]
    
    for i,word in enumerate(words[1:]):
        # 끝말이 이어지거나 사용한 단어집합에 없다면, 직전 단어를 바꿔주고 사용한 단어에 추가
        if (w[-1]==word[0]) and (word not in used_words):
            w = word
            used_words.add(word)
        # 그렇지 않다면, 잘린 첫 항을 생각해서 인덱스를 k로 맞춰주고 정답 리턴
        else:
            k = i+1 # k는 실제 순서
            return [k%n+1,k//n+1]
    # 반복문을 지나쳤다면 정상적이므로 [0,0] 리턴
    return [0,0]
   