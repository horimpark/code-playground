def service(score):
    scores = sum([int(x) for x in score.split(':')])
    target_value = 5 if scores < 40 else 2
    scores = 41 - scores if scores > 40 else scores
    if (scores // target_value) == 0 or (scores // target_value) % 2 == 0:
        return "first"
    else:
        return "second"
