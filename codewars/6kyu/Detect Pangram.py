def is_pangram(st):
    return len(set(filter(str.isalpha, st.lower()))) == 26


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog."))  # True
    print(is_pangram("This is not a pangram."))  # False
    print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))  # True
