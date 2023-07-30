def buildApartment(k, n):
    apartment = [[i for i in range(n + 1)] for _ in range(k + 1)]
    for floor_idx in range(len(apartment)):
        if floor_idx == 0: continue
        for room_idx in range(len(apartment[floor_idx])):
            if room_idx == 0: continue
            apartment[floor_idx][room_idx] = apartment[floor_idx - 1][room_idx] + apartment[floor_idx][room_idx - 1]
    return apartment

#1호 부터 14호, 0층 부터 14층
apartment = buildApartment(15, 15)
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n])
