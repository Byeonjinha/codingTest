import copy

temptable=[]
table2=[]
table3=[]
def solution(table, languages, preference):
    for i in table:
        p = i.split(" ")
        table3.append(p[0])
        for i2 in p:
            for i3 in languages:
                if i3==i2:
                    temptable.append((len(p)-p.index(i2))*preference[languages.index(i2)])
        table2.append(copy.deepcopy(sum(temptable)))
        temptable.clear()
    table4= list(zip(table3,table2))
    table4.sort( key= lambda x:(-x[1] , x[0]))
    return (table4[0][0])

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages= ["JAVA", "JAVASCRIPT"]
preference=[7, 5]
solution(table, languages, preference)