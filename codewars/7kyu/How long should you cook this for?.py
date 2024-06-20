import math

# 제출


def cooking_time(needed_power, minutes, seconds, power):
    needed_power = int(needed_power.split("W")[0])
    new_power = int(power.split("W")[0])
    new_power_time = needed_power * (60 * minutes + seconds) / new_power
    needed_minutes = int(new_power_time // 60)
    needed_seconds = int(math.ceil(new_power_time % 60))
    if needed_seconds == 60:
        needed_minutes = needed_minutes + 1
        needed_seconds = 0
    return f"{needed_minutes} minutes {needed_seconds} seconds"


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(cooking_time("600W", 4, 20, "800W"), "3 minutes 15 seconds")
        test.assert_equals(cooking_time("800W", 3, 0, "1200W"), "2 minutes 0 seconds")
        test.assert_equals(cooking_time("100W", 8, 45, "50W"), "17 minutes 30 seconds")
        test.assert_equals(cooking_time("7500W", 0, 5, "600W"), "1 minutes 3 seconds")
        test.assert_equals(cooking_time("450W", 3, 25, "950W"), "1 minutes 38 seconds")
        test.assert_equals(cooking_time("21W", 64, 88, "25W"), "55 minutes 0 seconds")
        test.assert_equals(cooking_time("83W", 61, 80, "26W"), "199 minutes 0 seconds")


# %%
