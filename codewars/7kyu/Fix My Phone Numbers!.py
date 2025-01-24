def is_it_a_num(s: str) -> str:
    num = ''.join([x for x in s if x.isdigit()])
    if num.startswith("0") and len(num) == 11:
        return num
    else:
        return "Not a phone number"