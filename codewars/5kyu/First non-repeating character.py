from collections import Counter


def first_non_repeating_letter(s):
    print(s)
    if not s:
        return s
    ss = s.lower()
    ss_cnt = {k: v for k, v in Counter([x for x in ss]).items() if v == 1}
    if not ss_cnt:
        return ""
    for i, x in enumerate(ss):
        if x in ss_cnt:
            return s[i]
