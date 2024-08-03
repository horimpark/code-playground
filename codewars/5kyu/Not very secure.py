def alphanumeric(password):
    if not password:
        return False
    for x in password:
        if x.isalpha() or x.isdigit():
            continue
        else:
            return False
    return True


# %%
# isalnum 이 있구나..
# def alphanumeric(string):
#     return string.isalnum()
