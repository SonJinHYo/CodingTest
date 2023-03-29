def solution(id_pw, db):
    ID,PW = id_pw
    db_dict = {}
    for i,p in db:
        db_dict[i] = p
    if ID in db_dict:
        if db_dict[ID]==PW:
            return 'login'
        return 'wrong pw'            
    return 'fail'
