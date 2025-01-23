from collections import Counter

def xo(s):
    s = s.lower()
    if all(x not in s for x in ["o", "x"]):
        return True
    else:
        count_s = Counter(s)
        if count_s["o"] == count_s['x']:
            return True
        else:
            return False