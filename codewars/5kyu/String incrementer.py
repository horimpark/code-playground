def increment_string(strng):
    strng_list = [x for x in strng]
    rev_strng_list = [x for x in reversed(strng_list)]

    rev_digits = []
    not_digits = ""
    for i, x in enumerate(rev_strng_list):
        if not x.isdigit():
            not_digits = strng[: len(strng) - i]
            break
        else:
            rev_digits.append(x)

    if not rev_digits:
        return strng + "1"

    digits = "".join([x for x in reversed(rev_digits)])
    print(digits, not_digits)
    next_digits = str(int(digits) + 1)
    if len(digits) > len(next_digits):
        return (
            not_digits
            + "".join(["0" for x in range(len(digits) - len(next_digits))])
            + f"{next_digits}"
        )
    else:
        return not_digits + f"{next_digits}"


# 공부한 코드
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
