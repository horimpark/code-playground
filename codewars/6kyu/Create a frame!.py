def frame(text, char):
    max_len = max([len(x) for x in text])
    frame_max_len = max_len + 4
    res = [char*frame_max_len]
    for x in text:
        margin_space = ' '*(max_len - len(x))
        res.append(f"{char} {x}{margin_space} {char}")
    res.append(char*frame_max_len)
    return '\n'.join(res)
