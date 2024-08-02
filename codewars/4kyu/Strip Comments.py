def strip_comments(strng, markers):
    lines = strng.split("\n")
    for i in range(len(lines)):
        for m in markers:
            if m in lines[i]:
                lines[i] = lines[i].split(m)[0].rstrip()
            else:
                lines[i] = lines[i].rstrip()
    return "\n".join(lines)
