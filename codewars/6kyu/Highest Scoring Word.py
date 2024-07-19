def high(x):
    score_book = {x: i + 1 for i, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    split_x = x.split(" ")
    scores = []
    for word in split_x:
        s = 0
        for x in word:
            s += score_book[x]
        scores.append(s)

    return split_x[scores.index(max(scores))]


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(high("man i need a taxi up to ubud"), "taxi")
        test.assert_equals(high("what time are we climbing up the volcano"), "volcano")
        test.assert_equals(high("take me to semynak"), "semynak")
        test.assert_equals(high("aa b"), "aa")
        test.assert_equals(high("b aa"), "b")
        test.assert_equals(high("bb d"), "bb")
        test.assert_equals(high("d bb"), "d")
        test.assert_equals(high("aaa b"), "aaa")
