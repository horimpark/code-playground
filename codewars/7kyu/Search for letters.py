def change(st):
    abc = {x: '0'  for _, x in enumerate('abcdefghijklmnopqrstuvwxyz')}
    for x in st:
        x = x.lower() if x.isalpha() else x
        if x in abc:
            abc[x] = '1'
    return ''.join(abc.values())
    
