def abstract(word):
    if len(word) >=4:
        return f"{word[0]}{len(word[1:-1])}{word[-1]}"
    else:
        return word

def abbreviate(s):
    no_alpha_idx = [i for i, x in enumerate(s) if not x.isalpha()]
    split_s = []
    for i, idx in enumerate(no_alpha_idx):
        if i == 0:
            split_s.append(s[:idx])
            split_s.append(s[idx:idx+1])
        else:
            split_s.append(s[no_alpha_idx[i-1]+1:idx])
            split_s.append(s[idx:idx+1])
        if i == len(no_alpha_idx) - 1:
            split_s.append(s[idx+1:])
    if not split_s:
        return abstract(s)
    else:
        res = [abstract(x) for x in split_s]
        return ''.join(res)
