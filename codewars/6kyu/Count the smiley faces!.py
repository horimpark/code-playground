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
