from collections import defaultdict

def solution(keymap, targets):
    answer = []
    key_dict = defaultdict()
    for key in keymap:
        for i,c in enumerate(key):
            key_dict[c] = min(key_dict[c],i+1) if c in key_dict else i+1
    for target in targets:
        result = 0
        for c in target:
            if c not in key_dict:
                result = -1
                break
            result+=key_dict[c]
        answer.append(result)
    return answer