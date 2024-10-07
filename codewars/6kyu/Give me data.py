def has_permission(user_info, accessing_data):
    if not user_info:
        return False
    info = dict()
    for x in user_info:
        split_x = x.split("_")
        name = split_x[0]

        answer = True if split_x[1] == "allow" else False
        if name in info and info[name] == False:
            continue
        info[name] = answer

    if accessing_data in info:
        return info[accessing_data]
    if "*" in info:
        return info["*"]
    return False
