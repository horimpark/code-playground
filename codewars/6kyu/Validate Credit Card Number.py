def validate(n):
    digits = [int(d) for d in str(n)]
    reversed_digits = digits[::-1]
    processed_digits = []

    for i, digit in enumerate(reversed_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                processed_digits.append(doubled - 9)
            else:
                processed_digits.append(doubled)
        else:
            processed_digits.append(digit)

    total_sum = sum(processed_digits)
    return total_sum % 10 == 0


if __name__ == "__main__":
    print(validate(123))
    print(validate(2121))
    print(validate(1230))
    print(validate(2121))
    print(validate(1234567890123456))
    print(validate(2121))