# ord()를 아는지 모르는지 물어보는 문제?

def alphabet_position(text):
    text = text.lower()
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            position = ord(char) - ord('a') + 1
            result.append(str(position))

    return ' '.join(result)


input_text = "The sunset sets at twelve o' clock."
output_text = alphabet_position(input_text)
print(output_text)
