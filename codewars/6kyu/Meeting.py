def meeting(s):
    meet = []
    for x in s.split(';'):
        f_name, l_name = x.split(':')
        meet.append(
            (l_name.upper(), f_name.upper())
        )
    sort_meet = sorted(meet, key=lambda x: (x[0], x[1]))
    res = ""
    for k, v in sort_meet:
        res += f"({k}, {v})"
    return res