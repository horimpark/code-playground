def check_exam(arr1, arr2):
    score = 0
    for a, b in zip(arr1, arr2):
        if b == "":
            score += 0
        elif a == b:
            score += 4
        else:
            score -= 1
    return score if score > 0 else 0
