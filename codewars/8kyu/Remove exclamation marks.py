def remove_exclamation_marks(s):
    s = [x for x in s if x != "!"]
    return "".join(s)
