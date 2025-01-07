def decode(string_):
    if not isinstance(string_, str):
        return "Input is not a string"

    decoded_message = ""
    for char in string_:
        if char.isalpha():
            if char.islower():
                decoded_message += chr(ord('z') - (ord(char) - ord('a')))
            else:
                decoded_message += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            decoded_message += char

    return decoded_message


if __name__ == "__main__":
    print(decode("abc"))  # zyx
    print(decode("ABC"))  # ZYX
    print(decode("aBc"))  # zYx
    print(decode("a1c"))  # z1c
    print(decode(123))  # Input is not a string
    print(decode("123"))  # 123