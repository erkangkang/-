def binary_to_ascii(binary_string):
    ascii_string = ""
    binary_list = binary_string.split()

    for binary in binary_list:
        decimal = int(binary, 2)
        ascii_char = chr(decimal)
        ascii_string += ascii_char

    return ascii_string

# 二进制字符串
binary_string = '01100110 01101100 01100001 01100111 01111011 01100110 01100010 00110001 00111001 00110111 00110101 01100101 00111001 01100011 00111001 00110011 00110010 00111000 00110000 00110111 01100110 00110111 00111001 00110100 00111001 00110011 00111001 00110101 01100100 01100101 00110100 01100100 00110100 01100001 01100010 00110011 00110001 01111101'

# 转换为ASCII码
ascii_result = binary_to_ascii(binary_string)

print("转换结果：", ascii_result)