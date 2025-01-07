def expanded_form(num):
    return " + ".join(str(n) + str(0) * (len(str(num))-1-i) for i, n in enumerate([k for k in str(num)]) if int(n))