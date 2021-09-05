def solution(absolutes, signs):
    for i in range(len(signs)):
        if not signs[i] == True:
            absolutes[i]*=-1
    print(sum(absolutes))
    return sum(absolutes)

#
# absolutes = [4,7,12]
# signs = ['true','false','true']

absolutes = [1,2,3]
signs =['false','false','true']

solution(absolutes, signs)

