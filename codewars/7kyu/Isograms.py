def is_isogram(s):
    s = s.lower()
    char_set = set()

    for char in s:
        if char in char_set:
            return False
        char_set.add(char)

    return True


if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))  # True
    print(is_isogram("aba"))  # False
    print(is_isogram("moOse"))  # False
    print(is_isogram("isogram"))  # True
