"""Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (
well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false
"""

def check_brackets(text: str):
    while True:
        copy_text = text
        copy_text = copy_text.replace("()", "")
        copy_text = copy_text.replace("[]", "")
        copy_text = copy_text.replace("{}", "")
        if copy_text == text:
            return False
        if len(copy_text) == 0:
            return True
        text = copy_text



print(check_brackets("((()"))