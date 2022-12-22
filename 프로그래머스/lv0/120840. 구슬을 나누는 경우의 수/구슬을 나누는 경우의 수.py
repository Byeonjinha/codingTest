def solution(balls, share):
    nP = 1
    mP = 1
    n = balls
    m = share
    while balls > 1:
        nP *= balls
        balls -= 1
    while share > 1:
        mP *= share
        share -= 1
    nMm = n - m
    nMmP = 1
    while nMm > 1:
        nMmP *= nMm
        nMm -= 1
    return nP / (nMmP * mP)