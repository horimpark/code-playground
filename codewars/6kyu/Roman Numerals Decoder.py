def solution(roman : str) -> int:
    roman_dict = {
        "M": 1000, "D": 500, "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1
    }
    
    result = 0
    pre = 0
    for x in reversed(roman):
        now = roman_dict[x]
        if now >= pre:
            result += now
        else:
            result -= now
        pre = now
        
    return result