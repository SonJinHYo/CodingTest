def solution(elements):
    answer = set(elements)
    for n in range(2,len(elements)):
        new_elements = elements+elements[:n]
        answer.update([sum(new_elements[i:i+n]) for i in range(len(elements))])
    answer.add(sum(elements))
    return len(answer)