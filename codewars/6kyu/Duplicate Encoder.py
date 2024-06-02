from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    w_list = [x for x in word]
    w_cnt = Counter(w_list)
    print(w_cnt)
    result = "".join([")" if w_cnt[x] != 1 else "(" for x in w_list])

    return result

import codewars_test as test

@test.describe("Duplicate Encoder")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(duplicate_encode("din"), "(((")
        test.assert_equals(duplicate_encode("recede"), "()()()")
        test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
        test.assert_equals(duplicate_encode("(( @"), "))((")



