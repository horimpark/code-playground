import codewars_test as test

# 6/18 제출


# 명시적으로 tuple로 반환해야 함, test 코드에 명시적으로 ecode(s)[0] 식으로 호출하기 때문
def encode(s):
    if s == "":
        return ("", 0)
    else:
        sorted_total = sorted([s[i + 1 :] + s[:i] + s[i] for i in range(len(s))])
        print(f"string : {s}")
        print(sorted_total)
        return ("".join([x[-1] for x in sorted_total]), sorted_total.index(s))


def decode(s, n):
    if s == "":
        return ""
    sorted_total = [""] * len(s)
    for _ in range(len(s)):
        sorted_total = sorted([s[i] + sorted_total[i] for i in range(len(s))])
    print(f"string : {s}, index : {n}")
    print(sorted_total)
    return sorted_total[n]


test.assert_equals(encode("bananabar"), ("nnbbraaaa", 4))
test.assert_equals(encode("Humble Bundle"), ("e emnllbduuHB", 2))
test.assert_equals(encode("Mellow Yellow"), ("ww MYeelllloo", 1))
test.assert_equals(decode("nnbbraaaa", 4), "bananabar")
test.assert_equals(decode("e emnllbduuHB", 2), "Humble Bundle")
test.assert_equals(decode("ww MYeelllloo", 1), "Mellow Yellow")
