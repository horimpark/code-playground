from preloaded import MORSE_CODE


def decode_morse(morse_code):
    split_morse = morse_code.split("   ")
    res = []

    for x in split_morse:
        x_split = x.split(" ")
        word = ""
        for y in x_split:
            if y:
                word += MORSE_CODE[y]
        res.append(word)
    return " ".join(res).strip()
