def valid_braces(string):
    while any(c in string for c in ["()", "{}", "[]"]):
        for c in ["()", "{}", "[]"]:
            string = string.replace(c, '')

    if string:
        return False
    else:
        return True