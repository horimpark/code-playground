def in_array(array1, array2):
    res = []
    for x in array1:
        for y in array2:
            if x in y:
                res.append(x)
                break
    return sorted(set(res))


def in_array(array1, array2):
    answer = []
    for a1 in array1:
        if any(a1 in a2 for a2 in array2) and a1 not in answer:
            answer.append(a1)
    return sorted(answer)