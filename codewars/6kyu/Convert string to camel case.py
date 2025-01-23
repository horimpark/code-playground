def to_camel_case(text):
    answer = ""
    upper = False
    for t in text:
        if t.isalpha():
            if upper:
                t = t.upper()
                upper = False
            answer += t
        else:
            upper = True
    return answer


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))  # theStealthWarrior
    print(to_camel_case("The_Stealth_Warrior"))  # TheStealthWarrior
    print(to_camel_case("A-B-C"))  # ABC
    print(to_camel_case("a-b-c"))  # aBC
    print(to_camel_case("a b c"))  # a b c
