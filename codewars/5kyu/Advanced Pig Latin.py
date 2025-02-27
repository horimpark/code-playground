def translate(sentence):
    words = sentence.split(" ")

    res = []
    for w in words:
        vowel_idx = [
            i for i, x in enumerate(w) if x.lower() in ("a", "e", "i", "o", "u")
        ]
        vowel_idx = vowel_idx[0] if vowel_idx else -1
        is_upper = True if w[0].isupper() else False

        no_w_idx = [i for i, x in enumerate(w) if not x.isalpha()]
        no_w_idx = no_w_idx[0] if no_w_idx else -1

        n_w = "" if no_w_idx == -1 else w[no_w_idx:]
        w = w if no_w_idx == -1 else w[:no_w_idx]
        if vowel_idx == 0:
            res.append(f"{w}way{n_w}")
        elif vowel_idx == -1:
            if w:
                res.append(f"{w}ay{n_w}")
            else:
                res.append(f"{n_w}")
        else:
            l = w[:vowel_idx].lower()
            r = w[vowel_idx:].lower()
            if is_upper:
                r = f"{r[0].upper()}{r[1:]}"
            res.append(f"{r}{l}ay{n_w}")
    result = " ".join(res)
    return result


# %%
from collections import deque
from re import sub, I

vowels = {*"AEIOUaeiou"}


def translate(sentence):
    return sub(r"[a-z]+", trans_word, sentence, flags=I)


def trans_word(m):
    word = deque(m[0])
    up = [c.isupper() for c in word]
    if word[0] in vowels:
        word.extend("w")
    elif {*word} & vowels:
        while word[0] not in vowels:
            word.append(word.popleft().lower())
    word.extend("ay")
    for i, u in enumerate(up):
        word[i] = word[i].upper() if u else word[i].lower()
    return "".join(word)
