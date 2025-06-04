def fire_and_fury(tweet):
    str_list = []
    for i in range(len(tweet)):
        if tweet[i:i+4] == "FIRE" or tweet[i:i+4] == "FURY":
            if str_list and str_list[-1][0] == tweet[i:i+4]:
                str_list[-1][-1] = str_list[-1][-1] + 1
            else:
                str_list.append([tweet[i:i+4], 1])
    if not str_list or any(x not in "EFIRUY" for x in tweet):
        return "Fake tweet."
    res = []
    for w, c in str_list:
        if w == "FURY":
            target = "" if c==1 else "really " * (c-1)
            res.append(
                f"I am {target}furious."
            )
        elif w == "FIRE":
            target = "" if c==1 else "you and " * (c-1)
            res.append(
                f"{target}you are fired!"
            )
    return " ".join([f"{x[0].upper()}{x[1:]}" for x in res])
