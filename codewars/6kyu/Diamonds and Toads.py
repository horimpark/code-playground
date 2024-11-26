def diamonds_and_toads(sentence, fairy):
    if fairy == 'good':
        result = {"ruby": 0, "crystal": 0}
        for c in sentence:
            if c == 'r':
                result["ruby"] += 1
            elif c == "R":
                result["ruby"] += 2
            elif c == 'c':
                result["crystal"] += 1
            elif c == "C":
                result["crystal"] += 2
        return result
    elif fairy == 'evil':
        result = {"python": 0, "squirrel": 0}
        for c in sentence:
            if c == 'p':
                result["python"] += 1
            elif c == "P":
                result["python"] += 2
            elif c == 's':
                result["squirrel"] += 1
            elif c == "S":
                result["squirrel"] += 2
        return result

    return None


if __name__ == "__main__":
    print(diamonds_and_toads("Ruby is fun!", "good"))  # {'ruby': 2, 'crystal': 0}
    print(diamonds_and_toads("Ruby is fun!", "evil"))  # {'python': 0, 'squirrel': 0}
    print(diamonds_and_toads("Crystals are great!", "good"))  # {'ruby': 0, 'crystal': 2}
    print(diamonds_and_toads("Crystals are great!", "evil"))  # {'python': 0, 'squirrel': 0}

