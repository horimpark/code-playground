def solution(*args):
    if not args:
        return False
    elif len(args) != len(set(args)):
        return True
    else:
        return False
