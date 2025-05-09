def decode(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_dict = {x: y for x, y in zip(abc, reversed(abc))}
    
    res = []
    for x in message:
        if x in abc_dict:
            res.append(abc_dict[x])
        else:
            res.append(x)
    return ''.join(res)
