def validate_pin(pin):
    return True if pin.isdigit() and (len(pin) == 4 or len(pin) == 6) else False


if __name__ == "__main__":
    print(validate_pin("1234"))  # True
    print(validate_pin("12345"))  # False
    print(validate_pin("a234"))  # False
