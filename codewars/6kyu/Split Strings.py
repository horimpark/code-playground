def solution(s):
    print(f"length : {s}, {len(s)}")
    result = []
    for x in range(0, len(s), 2):
        result.append(s[x : x + 2])
    if not result:
        return result

    if len(result[-1]) == 1:
        result[-1] += "_"

    return result
