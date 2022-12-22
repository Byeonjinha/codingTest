def solution(dots):
    minX, minY, maxX, maxY = 1000, 1000, -1000, -1000
    for x, y in dots:
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
    return (maxX - minX) * (maxY - minY)