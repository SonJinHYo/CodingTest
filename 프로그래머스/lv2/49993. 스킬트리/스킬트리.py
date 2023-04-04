def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        tmp = ''.join([s for s in sk if s in skill])
        if skill[:len(tmp)] == tmp:
            answer+=1
    return answer