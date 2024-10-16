def letter_pattern(words):
    if len(words) == 1:
        return words[0]
    else:
        res = ""
        for i in range(len(words[0])):
            if len(set([words[x][i] for x in range(len(words))])) == 1:
                res += [words[x][i] for x in range(len(words))][0]
            else:
                res += "*"
        return res


# %%
# def letter_pattern(words):
# 	return ''.join(e[0] if len(set(e)) == 1 else '*' for e in zip(*words))
