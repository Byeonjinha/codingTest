def solution(participant, completion):
    try:
        for i in participant:
            completion.remove(i)
    except:
        pass
    finally:
        return i
