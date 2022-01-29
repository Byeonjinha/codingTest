from collections import deque


def solution(bridge_length, weight, truck_weights):
    temp = truck_weights
    truck_weights = deque(truck_weights)
    bridge_length = deque([0]*bridge_length)
    dochak=[]

    count=0
    going_truck = "aaa"
    n=0
    while dochak!=temp:
        ss=list(bridge_length)
        if len(truck_weights) !=0 and going_truck == "aaa":
            going_truck = truck_weights.popleft()
        elif len(truck_weights) ==0 and going_truck == "aaa" :
            going_truck = 0

        ss2 = sum(ss[-(len(bridge_length)-1):])

        if  (ss2+going_truck) <=weight:
            bridge_length.append(going_truck)
            going_truck = "aaa"
            b=bridge_length.popleft()
            if b!=0:
                dochak.append(b)
            count+=1

        else:
            bridge_length.append(0)
            b=bridge_length.popleft()
            if b!=0:
                dochak.append(b)
            count+=1
        n+=1

    return n




bridge_length =100
weight =100
truck_weights = 		[10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)