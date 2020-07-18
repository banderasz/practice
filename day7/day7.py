"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_code_pos(code: str):
    count = 1
    for i in range(len(code)):
        if i > 0:
            if int(code[i-1:i+1]) <= 26:
                count += 1
    return count

print(count_code_pos('11123'))