def compose(s1, s2):
    split_s1 = s1.split("\n")
    split_s2 = s2.split("\n")
    length = len(split_s1)

    strng = []
    for i in range(length):
        new_str = f"{split_s1[i][:i+1]}{split_s2[-i-1][:length-i]}"
        strng.append(new_str)
    return "\n".join(strng)
