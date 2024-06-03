def same_structure_as(original, other):
    def transform_zero(data):
        if isinstance(data, list):
            for i in range(len(data)):
                data[i] = transform_zero(data[i])
        else:
            data = 0
        return data

    og_trans = transform_zero(original)
    nw_trans = transform_zero(other)
    if og_trans == nw_trans:
        return True
    else:
        return False


import codewars_test as test

test.assert_equals(
    same_structure_as([1, [1, 1]], [2, [2, 2]]), True, "[1,[1,1]] same as [2,[2,2]]"
)
test.assert_equals(
    same_structure_as([1, [1, 1]], [[2, 2], 2]),
    False,
    "[1,[1,1]] not same as [[2,2],2]",
)
