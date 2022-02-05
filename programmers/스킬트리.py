from collections import deque
def solution(skill, skill_trees):
    skill = deque(skill)
    count=0
    for i in range(len(skill_trees)):
        temp = skill.copy()
        K = temp.popleft()
        a=True
        for j in range(len(skill_trees[i])):

            if skill_trees[i][j] in temp:
                a= False
                break
            if K== skill_trees[i][j]:
                if len(temp) == 0:
                    break
                K = temp.popleft()
                if len(temp) ==0:
                    break
        if a==True:
            count += 1
    answer = count
    return answer


skill	= "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)