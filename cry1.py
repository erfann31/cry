def text_to_binary(text):
    binary = ""
    for char in text:
        binary += bin(ord(char))[2:].zfill(8)  # convert each character to binary
    return binary


def split_binary(binary):
    midpoint = len(binary) // 2
    left = binary[:midpoint]
    right = binary[midpoint:]
    return left, right


def xor_binary(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "00"
        else:
            result += "1"
    return result


def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]
        text += chr(int(byte, 2))
    return text


ciphertext, key = input().strip().split()
binary = text_to_binary(ciphertext)
left, right = split_binary(binary)
result = xor_binary(xor_binary(left, key), right) + left
print(binary_to_text(result))
