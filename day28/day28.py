"""Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of
strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between
each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as
equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k =
16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def justify(words: list, k: int):
    text = ""
    row = []
    length = 0
    for word in words:
        if len(word) + len(row) + length <= k:
            row.append(word)
            length += len(word)
        else:
            evenly = (k - length) // (len(row)-1)
            extra = (k - length) % (len(row)-1)
            for i in range(len(row)-1):
                if extra:
                    text += row[i] + " " * (evenly + 1)
                    extra -= 1
                else:
                    text += row[i] + " " * (evenly)
            text += row[-1]
            text += "\n"
            row = [word]
            length = len(word)
    if len(row) > 1:
        evenly = (k - length) // (len(row) - 1)
        extra = (k - length) % (len(row) - 1)
        for i in range(len(row) - 1):
            if extra:
                text += row[i] + " " * (evenly + 1)
                extra -= 1
            else:
                text += row[i] + " " * (evenly)
        text += row[-1]
    else:
        text += " "*(k-len(row[-1])) + row[-1]
    return text


print(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))
text_list = "Write an algorithm to justify text. Given a sequence of words and an integer line length k, " \
            "return a list of strings which represents each line, fully justified.".split(" ")

print(justify(text_list, 32))
