def calculate_rwx(n):
    answer = 0
    if "r" in n:
        answer += 4
    if "w" in n:
        answer += 2
    if "x" in n:
        answer += 1
    return str(answer)


def chmod_calculator(perm):
    return "".join([calculate_rwx(perm.get("user", "")),
                    calculate_rwx(perm.get("group", "")),
                    calculate_rwx(perm.get("other", ""))])