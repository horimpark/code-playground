def word_search(query, seq):
    result = [x for x in seq if query.lower() in x.lower()]
    return result if result else ["None"]


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            word_search("ab", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"]
        )
        test.assert_equals(
            word_search("aB", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"]
        )
        test.assert_equals(
            word_search("ab", ["za", "aB", "Abc", "zAB", "zbc"]), ["aB", "Abc", "zAB"]
        )
        test.assert_equals(
            word_search("abcd", ["za", "aB", "Abc", "zAB", "zbc"]), ["None"]
        )
