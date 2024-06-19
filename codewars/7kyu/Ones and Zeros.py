def binary_array_to_number(arr):
    arr.reverse()
    sum = 0
    for i, x in enumerate(arr):
        sum += (2**i) * x
    return sum


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
        test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
        test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
        test.assert_equals(binary_array_to_number([0,1,1,0]), 6)