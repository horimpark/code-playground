def ordinal(number, brief=False):
    str_n = str(number)
    res = "th" if str_n[-1] not in ("1", "2", "3") else "?"
    if res == "?":
        if len(str_n) > 1 and str_n[-2] == "1":
            res = "th"
        else:
            if str_n[-1] == "1":
                res = "st"
            elif str_n[-1] == "2":
                res = "nd"
            elif str_n[-1] == "3":
                res = "rd"

    if brief and res not in ("st", "th"):
        return "d"
    else:
        return res


# def ordinal(n, brief=False):
#     n %= 100
#     if 9 < n < 20:
#         return "th"
#     n %= 10
#     if n == 1:
#         return "st"
#     if n == 2:
#         return "nd"[brief:]
#     if n == 3:
#         return "rd"[brief:]
#     return "th"
