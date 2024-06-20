# 제출
def rgb(r, g, b):
    def transformer(x):
        if x < 0:
            return "00"
        elif x > 255:
            return "FF"
        else:
            h = hex(x)[2:].upper()
            if len(h) == 1:
                h = "0" + h
            return h

    return transformer(r) + transformer(g) + transformer(b)


# example code
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))
# i'm jotbab...

import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
