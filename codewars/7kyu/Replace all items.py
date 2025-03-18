def replace_str(s, f, r):
    if type(s) == int:
        return int(str(s).replace(str(f), str(r)))
    else:
        return s.replace(f, r)

def replace_all(obj, find, replace):
    if type(obj) == str:
        return obj.replace(find, replace)
    return [replace_str(o, find, replace) for o in obj]