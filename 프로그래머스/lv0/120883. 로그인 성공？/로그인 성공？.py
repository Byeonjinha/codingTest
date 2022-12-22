def solution(id_pw, db):
    answer = ''
    for userID, userPW in db:
        if id_pw[0] == userID and id_pw[1] == userPW :
            return "login"
        elif id_pw[0] == userID and id_pw[1] != userPW :
                return "wrong pw"
        else :
            "fail"
    return "fail"