def solution(polynomial):
    x = 0
    y = 0
    for i in polynomial.split(" + ") :
        if i == "x":
            x += 1
        elif i[-1] == "x":
            x += int(i[:len(i)-1])
        else :
            y += int(i)
    if x == 0 :
        return str(y)
    elif x == 1 and y == 0:
        return "x"
    elif x == 1 and y != 0:
        return "x + " + str(y)
    elif y == 0 :
        return str(x) + "x"
    
    return str(x)+"x + " + str(y)