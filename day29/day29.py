"""Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
solely of alphabetic characters. You can assume the string to be decoded is valid. """

def encode(text: str):
    code = ""
    calc = 1
    for i in range(len(text)):
        if i +1 < len(text):
            if text[i] == text[i+1]:
                calc +=1
            else:
                code += str(calc) + text[i]
                calc = 1
        else:
            code += str(calc) + text[i]
            calc = 1
    return code

def decode(code: str):
    text = ""
    last_index = 0
    for i in range(len(code)):
        if code[i].isalpha():
            text += code[i]*int(code[last_index:i])
            last_index = i+1
    return text






print(decode(encode("AAAABBBCCDAA")))