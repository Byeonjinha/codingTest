def solution(code):
    state = True
    ret = ''
    for idx, c in enumerate(code):
        if c == "1":
            state = not state
        else:
            if state:
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                if idx % 2 == 1:
                    ret += code[idx]
    if len(ret) == 0: return "EMPTY"
    else: return ret