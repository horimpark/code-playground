import re


def is_multiple_of_3(binary_string):
    multipleof3Regex = re.compile(r'^(0*|0*(1(01*0)*1)*)*$')

    if multipleof3Regex.match(binary_string):
        return True
    else:
        return False


# 테스트 케이스
test_cases = ['000', '001', '011', '110', ' abc ']
results = {tc: is_multiple_of_3(tc) for tc in test_cases}
print(results)