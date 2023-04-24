def solution(genres, plays):
    album = {}
    answer = []
    
    
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = {'total':plays[i],i:plays[i]}
        else:
            album[genres[i]]['total']+=plays[i]
            album[genres[i]][i] = plays[i]
    album_list = sorted(album.values(),key = lambda x: -x['total'])
    for i in album_list:
        del i['total']
        for index,cnt in sorted(i.items(),key = lambda x: -x[1])[:2]:
            answer.append(index)
            
    return answer
