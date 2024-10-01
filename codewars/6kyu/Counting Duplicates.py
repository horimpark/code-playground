from collections import Counter


def duplicate_count(text):
    counter = Counter([t.lower() for t in text])
    dup_list = [c for a, c in counter.items() if c > 1]
    return len(dup_list)


if __name__ == "__main__":
    print(duplicate_count("abcde"))  # 0
    print(duplicate_count("aabbcde"))  # 2
    print(duplicate_count("aabBcde"))  # 2
    print(duplicate_count("indivisibility"))  # 1
    print(duplicate_count("Indivisibilities"))  # 2
    print(duplicate_count("aA11"))  # 2
    print(duplicate_count("ABBA"))  # 2