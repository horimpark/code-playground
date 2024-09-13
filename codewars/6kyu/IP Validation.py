def is_valid_IP(strng):
    split_str = strng.split(".")
    return (
        True
        if len(split_str) == 4
        and all(
            x.isdigit() and int(x) >= 0 and int(x) <= 255 and x == str(int(x))
            for x in split_str
        )
        else False
    )
