def even_chars(st): 
    return [x for i, x in enumerate(st) if (i+1)%2==0] if len(st) > 1 and len(st) <= 100 else "invalid string"
