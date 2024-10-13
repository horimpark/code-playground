def password(st):
    if (
        any(x.isupper() for x in st)
        and any(x.islower() for x in st)
        and any(x.isdigit() for x in st)
        and len(st) >= 8
    ):
        return True
    else:
        return False
