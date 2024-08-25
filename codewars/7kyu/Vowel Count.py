def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiou')


if __name__ == "__main__":
    print(get_count("abracadabra"))  # 5