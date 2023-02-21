from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    flag = True 
    while (cards1 or cards2) and goal and flag:
        word = goal.popleft()
        flag = False
        if len(cards1) != 0:
            if word == cards1[0]: cards1.popleft(); flag = True; word = ""
        if len(cards2) != 0:
            if word == cards2[0]: cards2.popleft(); flag = True; word = ""
    if goal or word != "":
        return "No"
    return "Yes"