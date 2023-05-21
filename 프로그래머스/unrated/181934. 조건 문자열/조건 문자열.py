def solution(ineq, eq, n, m):
    try :
        if (eval(str(n) + ineq + eq + str(m))):
            return 1
    except:
          if (eval(str(n) + ineq + str(m))):
                     return 1
    return 0