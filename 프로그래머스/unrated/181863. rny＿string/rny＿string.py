def solution(rny_string):
    rny_string = list(rny_string)
    while 'm' in rny_string:
        rny_string[rny_string.index('m')] = 'rn'
    return ''.join(rny_string)