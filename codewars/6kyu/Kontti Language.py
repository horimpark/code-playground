def kontti(s):
    print(s)
    s_split = s.split(" ")
    res = []

    for w in s_split:
        vowel_idx = [
            i for i, x in enumerate(w) if x in "aeiouy" or x.lower() in "aeiouy"
        ]
        if not vowel_idx:
            res.append(w)
        else:
            start = vowel_idx[0]
            res.append(f"ko{w[start+1:]}-{w[:start+1]}ntti")
    return " ".join(res)
