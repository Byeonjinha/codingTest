def generate_ciphertext(num):
    ciphertext_count = int(input())
    origin_ciphertext = input().split()
    command_count = int(input())
    commands = input().split("I")[1:]

    for command in commands:
        start_idx, count, *ciphertext = command.split(" ")[1:]
        for idx in range(int(start_idx), int(start_idx) + int(count)):
            origin_ciphertext.insert(idx, ciphertext[idx - int(start_idx)])
    return "#{} {}".format(num, " ".join(origin_ciphertext[:10]))

for i in range(1, 11):
    print(generate_ciphertext(i))