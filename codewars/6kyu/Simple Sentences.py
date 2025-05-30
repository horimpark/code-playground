def make_sentences(parts):
    res = []
    for x in range(len(parts)):
        if parts[x].isalpha() or parts[x].isdigit():
            res.append(' ')
            res.append(parts[x])
        elif parts[x] == ',':
            res.append(parts[x])
    res.append(".")
    return ''.join(res).strip()


# def make_sentences(parts):
#    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'
