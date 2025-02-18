def count_smileys(arr):
    valid = {"eyes": [":", ";"], "nose": ["-", "~"], "mouth": [")", "D"]}
    res = []
    for x in arr:
        is_valid = False
        if x[0] in valid["eyes"]:
            is_valid = True
        else:
            is_valid = False

        if len(x) == 3 and x[1] in valid["nose"] and x[2] in valid["mouth"]:
            is_valid = True
        elif x[1] in valid["mouth"]:
            is_valid = True
        else:
            is_valid = False

        if is_valid:
            res.append(x)

    return len(res)


def is_smile(x):
    if len(x) == 3:
        str_x = [i for i in x]
        if all(str_x[1] != n for n in ["-", "~"]):
            return False
    if any(x.startswith(i) for i in [";", ":"]) and any(x.endswith(i) for i in [')', 'D']):
        return True

def count_smileys(arr):
    return len([a for a in arr if is_smile(a)])