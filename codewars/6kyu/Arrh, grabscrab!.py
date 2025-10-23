def grabscrab(said, possible_words):
    res = []
    for word in possible_words:
        if len(word) == len(said) and sorted([x for x in said]) == sorted([x for x in word]):
            res.append(word)

    return res
