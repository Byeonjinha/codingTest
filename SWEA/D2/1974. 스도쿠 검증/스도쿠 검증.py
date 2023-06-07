def is_valid_sudoku(puzzle):
    # 가로 방향 검사
    for row in puzzle:
        if len(set(row)) != 9:
            return 0

    # 세로 방향 검사
    for col in range(9):
        if len(set(puzzle[row][col] for row in range(9))) != 9:
            return 0

    # 3x3 격자 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [puzzle[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if len(set(block)) != 9:
                return 0

    return 1


T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    result = is_valid_sudoku(puzzle)

    print(f"#{tc} {result}")
