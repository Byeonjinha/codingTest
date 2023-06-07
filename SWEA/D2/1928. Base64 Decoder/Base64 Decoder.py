T = int(input())

def base64_decode(encoded_str):
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    decoded_str = ""
    buffer = 0
    buffer_size = 0

    for char in encoded_str:
        if char == '=':
            break

        value = base64_table.index(char)
        buffer = (buffer << 6) | value
        buffer_size += 6

        while buffer_size >= 8:
            buffer_size -= 8
            decoded_char = (buffer >> buffer_size) & 255
            decoded_str += chr(decoded_char)

    return decoded_str

for tc in range(1, T + 1):
    encoded_str = input()
    decoded_str = base64_decode(encoded_str)
    print(f"#{tc} {decoded_str}")
