from collections import Counter

score_dict = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


def score(dice):
    cnt = Counter(dice)
    total_score = 0
    print(cnt)
    for k, v in cnt.items():
        if v >= 3:
            m, n = v // 3, v % 3
            total_score += score_dict[k]
            v = n

        if k in (1, 5) and v != 0:
            total_score += score_dict[k] / 10 * v
    return total_score


import codewars_test as test


@test.describe("Example Tests")
def example_tests():
    @test.it("Example cases")
    def example_cases():
        test.assert_equals(score([5, 1, 3, 4, 1]), 250)
        test.assert_equals(score([1, 1, 1, 3, 1]), 1100)
        test.assert_equals(score([2, 3, 4, 6, 2]), 0)
        test.assert_equals(score([4, 4, 4, 3, 3]), 400)
        test.assert_equals(score([2, 4, 4, 5, 4]), 450)
