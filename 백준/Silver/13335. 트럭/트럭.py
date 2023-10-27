from collections import deque

n, w, l = map(int, input().split())

cars = deque(list(map(int, input().split())))

bridge = deque([0 for _ in range(w)])

answer = 0

def loadCar():
    global cars, bridge
    bridge[-1] = cars.popleft()

def moveCar():
    bridge.popleft()
    bridge.append(0)

def check_weight():
    global bridge, cars
    return sum(bridge) + cars[0] <= l

def check_car_empty():
    return len(cars) == 0

def check_bridge_empty():
    return sum(bridge) == 0

while not check_car_empty() or not check_bridge_empty():

    answer += 1
    moveCar()

    if not check_car_empty() and check_weight():
        loadCar()

print(answer)