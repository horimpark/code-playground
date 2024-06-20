def spin_words(sentence):
    result = []
    for x in sentence.split(" "):
        if len(x) > 4:
            result.append(x[::-1])
        else:
            result.append(x)
    return " ".join(result)
