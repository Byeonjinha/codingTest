sheet = [[-1 for _ in range(50)] for _ in range(50)]
mergeSheet = [[set([(y, x)]) for x in range(50)] for y in range(50)]

answer = []

def update(r, c, value):
    global sheet
    for y, x in mergeSheet[r][c]:
        sheet[y][x] = value
    return

def update2(value1, value2):
    for y in range(len(sheet)):
        for x in range(len(sheet[y])):
            if value1 == sheet[y][x]: sheet[y][x] = value2
    return

def merge(r1, c1, r2, c2):
    if sheet[r1][c1] == -1:
        mergeTmpSheet = set([(r1, c1), (r2, c2)])
        for y, x in mergeSheet[r1][c1]:
            mergeTmpSheet.update(set([(y, x)]))
        for y, x in mergeSheet[r2][c2]:
            mergeTmpSheet.update(set([(y, x)]))
        for y, x in mergeTmpSheet:
            mergeSheet[y][x].update(mergeTmpSheet)
        for y, x in mergeTmpSheet:
            sheet[y][x] = sheet[r2][c2]
            
    else:
        mergeSheet[r1][c1].update(mergeSheet[r2][c2])
        for y, x in mergeSheet[r1][c1]:
            mergeSheet[y][x].update(mergeSheet[r1][c1])
        for y, x in mergeSheet[r1][c1]:
            sheet[y][x] = sheet[r1][c1]
    return

def unmerge(r, c):
    for y, x in mergeSheet[r][c]:
        mergeSheet[y][x] = set([(y, x)])
        if r == y and c == x:
            continue
        else:
            sheet[y][x] = -1
    return

def sheetPrint(r, c):
    if sheet[r][c] == -1:
         answer.append("EMPTY")
    else:
        answer.append(sheet[r][c])
    return

def solution(commands):
    global answer
    
    for command in commands:
        command, *content = command.split()
        if command == "UPDATE":
            if len(content) == 2:
                update2(content[0], content[1])
            elif len(content) == 3:
                update(int(content[0]) - 1, int(content[1]) - 1, content[2])
                
        elif command == "MERGE":
            merge(int(content[0]) - 1, int(content[1]) - 1, int(content[2]) - 1, int(content[3]) - 1)
        elif command == "UNMERGE":
            unmerge(int(content[0]) - 1, int(content[1]) - 1)
        elif command == "PRINT":
            sheetPrint(int(content[0]) - 1, int(content[1]) - 1)
    
        
    return answer