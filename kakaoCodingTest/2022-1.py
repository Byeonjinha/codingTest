
def solution(id_list, report, k):
    reportlist={}
    report = list(set(report))
    singoza =[]
    gahaeza =[]

    for i in range(len(report)):
        k=report[i].split(" ")
        singoza.append(k[0])
        gahaeza.append(k[1])
    gahaezaa=list(set(gahaeza))
    print(gahaezaa)

    for i in range(len(report)):
        k = report[i].split(" ")
        print(reportlist)
        if k[0] in reportlist:
            print(k[0],k[1])
            reportlist[k[0]].append(k[1])

        reportlist[k[0]]=k[1]

id_list	=["muzi", "frodo", "apeach", "neo"]
report= ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
solution(id_list, report, k)