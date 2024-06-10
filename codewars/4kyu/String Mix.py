from collections import Counter


def mix(s1, s2):
    def count_char(text):
        return Counter(char for char in text if char.islower())

    s1_cnt = count_char(s1)
    s2_cnt = count_char(s2)

    result = []
    for c in "abcdefghijklmnopqrstuvwxyz":
        c1 = s1_cnt.get(c, 0)
        c2 = s2_cnt.get(c, 0)
        if c1 > 1 or c2 > 1:
            if c1 > c2:
                result.append(f"1:{c * c1}")
            elif c2 > c1:
                result.append(f"2:{c * c2}")
            else:
                result.append(f"=:{c * c1}")

    result.sort(key=lambda x: (-len(x), x))

    return "/".join(result)


import codewars_test as test


@test.describe("Mix")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(
            mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr"
        )
        test.assert_equals(
            mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
            "2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz",
        )
        test.assert_equals(
            mix("looping is fun but dangerous", "less dangerous than coding"),
            "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg",
        )
        test.assert_equals(
            mix(" In many languages", " there's a pair of functions"),
            "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt",
        )
        test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        test.assert_equals(mix("codewars", "codewars"), "")
        test.assert_equals(
            mix("A generation must confront the looming ", "codewarrs"),
            "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr",
        )
