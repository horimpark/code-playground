def valid_parentheses(paren_str):
    stack = 0
    for x in paren_str:
        if x == "(":
            stack += 1
        elif stack != 0 and x == ")":
            stack -= 1
        else:
            return False
    return True if stack == 0 else False
