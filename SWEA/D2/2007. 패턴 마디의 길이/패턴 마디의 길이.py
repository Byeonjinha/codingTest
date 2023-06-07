T = int(input())

def find_madi_length(string):
    for i in range(1, 11):
        if string[:i] == string[i:i+i]:
            return i
        
for i in range(1, T + 1):
    # 사용자로부터 문자열 입력 받기
    input_string = input()

    # 마디의 길이 찾기
    madi_length = find_madi_length(input_string)
    # 결과 출력
    print("#{} {}".format(i, madi_length))