def solution(myStr):
    myStr = myStr.replace("a","+").replace("b","+").replace("c","+").replace("++","+").split("+")
    # print(myStr)
    while "" in myStr:
        myStr.remove("")
    if len(myStr) == 0:
        myStr.append("EMPTY")
    return myStr